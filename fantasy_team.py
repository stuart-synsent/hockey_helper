import pandas as pd
import pulp
import json
from docopt import docopt


# Save team to file
def save_team_to_file(team, filename):
    with open(filename, "w") as f:
        json.dump(team, f)
    print(f"Team saved to {filename}")


# Load team from file
def load_team_from_file(filename):
    with open(filename, "r") as f:
        return json.load(f)


def select_team(players, budget, positions_needed, must_include=None, exclude_players=None, points_type="total"):
    # Create optimization problem
    prob = pulp.LpProblem("FantasyHockeyTeam", pulp.LpMaximize)

    # Create binary decision variables for all players
    player_vars = {row["Name"]: pulp.LpVariable(row["Name"], cat="Binary") for _, row in players.iterrows()}

    # Maximize total or average points based on user choice
    points_column = "Total Points" if points_type == "total" else "Avg"
    prob += pulp.lpSum(player_vars[row["Name"]] * row[points_column] for _, row in players.iterrows())

    # Total cost must be within budget
    prob += pulp.lpSum(player_vars[row["Name"]] * row["$"] for _, row in players.iterrows()) <= budget

    # Number of players per position
    for position, count in positions_needed.items():
        prob += pulp.lpSum(player_vars[row["Name"]] for _, row in players.iterrows() if row["Pos"] == position) == count

    # Include specific players
    if must_include:
        for player in must_include:
            prob += player_vars[player] == 1
            # Adjust the budget and position needed for included players
            player_row = players[players["Name"] == player].iloc[0]
            budget -= player_row["$"]
            positions_needed[player_row["Pos"]] -= 1

    # Exclude specific players
    if exclude_players:
        for player in exclude_players:
            prob += player_vars[player] == 0

    # and got for it!
    prob.solve()

    selected_team = []
    for _, row in players.iterrows():
        if player_vars[row["Name"]].value() == 1:
            selected_team.append(
                {
                    "Name": row["Name"],
                    "Pos": row["Pos"],
                    "team": row["team"],
                    "Avg": row["Avg"],
                    "Total Points": row["Total Points"],
                    "$": row["$"],
                    "Gp": row["Gp"],
                }
            )
    position_order = {"C": 1, "W": 2, "D": 3, "G": 4}

    # Sort team by the position order
    team = sorted(selected_team, key=lambda x: position_order[x["Pos"]])

    return team


def recommend_replacements(current_team, removed_player, budget_left, position, players, num_replacements=5):
    potential_replacements = players[
        (players["Name"] != removed_player)
        & (players["Pos"] == position)
        & (~players["Name"].isin([p["Name"] for p in current_team]))
        & (players["$"] <= budget_left)
    ]
    potential_replacements = potential_replacements.sort_values(by="Total Points", ascending=False)

    top_replacements = potential_replacements.head(num_replacements)
    return top_replacements


def display_team(team):
    position_order = {"C": 1, "W": 2, "D": 3, "G": 4}

    # Sort team by the position order
    sorted_team = sorted(team, key=lambda x: position_order[x["Pos"]])

    print("Current Team:")
    total_points = sum(player["Total Points"] for player in sorted_team)
    total_cost = sum(player["$"] for player in sorted_team)
    total_cost = "{:.2f}".format(total_cost)
    for i, player in enumerate(sorted_team):
        print(
            f"{i:2}. {player['Name']:15} - {player['Pos']:1} - {player['team']:3} - {player['Avg']:4} PPG - {player['$']:5} cost - Total Points: {player['Total Points']:6}"
        )

    print(f"\nTotal Points: {total_points}")
    print(f"Total Cost: {total_cost}")
    return sorted_team


def choose_player_to_remove(team):
    team = display_team(team)
    index = int(input("Enter the number of the player you want to remove: "))
    print(f"Removing {team[index]['Name']} from the team.")
    removed_player = team[index]
    return removed_player, index


def choose_replacement(replacements):
    print("\nTop 5 Replacements:")
    for i, (_, row) in enumerate(replacements.iterrows()):
        print(
            f"{i:2}. {row['Name']:15} - {row['Pos']:1} - {row['team']:3} - {row['Avg']:4} PPG - {row['$']:5} cost - Total Points: {row['Total Points']:6}"
        )
    choice = input("\nEnter the number of the replacement player (or type 'r' to revert): ")
    return choice


def main():
    doc = """
    Usage:
        fantasy_hockey.py [--must-include=<players>] [--exclude=<players>] [--points-type=<type>] [--minimum-games=<games>] [--budget=<budget>] [--load-team=<team>]

    Options:
        --must-include=<players>  Comma-separated list of players to include.
        --exclude=<players>       Comma-separated list of players to exclude.
        --points-type=<type>      The type of points to optimize ('total' or 'average') [default: total].
        --minimum-games=<games>   Minimum number of games played [default: 40].
        --budget=<budget>         Budget for the team [default: 50].
        --load-team=<team>        Load a previously saved team from the supplied file.
    """

    args = docopt(doc)

    must_include = args["--must-include"].split(",") if args["--must-include"] else []
    exclude_players = args["--exclude"].split(",") if args["--exclude"] else []
    points_type = args["--points-type"]
    minimum_games = int(args["--minimum-games"])
    budget = int(args["--budget"])

    file_path = "data/updated_players.csv"
    df = pd.read_csv(file_path)

    df = df[df["Gp"] >= minimum_games]
    players = df[["Name", "team", "Pos", "Avg", "$", "Gp"]]
    total_points = round(players["Gp"] * players["Avg"])
    players["Total Points"] = total_points
    positions_needed = {"C": 3, "W": 4, "D": 3, "G": 2}

    if args["--load-team"]:
        team_file = args["--load-team"]
        team = load_team_from_file(team_file)
        display_team(team)
    else:
        team_file = "fantasy_team.json"

        team = select_team(
            players,
            budget,
            positions_needed,
            must_include=must_include,
            exclude_players=exclude_players,
            points_type=points_type,
        )

        display_team(team)

    while True:
        # ask if they want to make changes:
        choice = input("Do you want to make changes to the team? (y/n): ")
        if choice.lower() == "n":
            break
        else:
            print("Let's make some changes to the team!\n")

        # Choose a player to remove
        removed_player, removed_index = choose_player_to_remove(team)

        # Calculate remaining budget
        budget_left = budget - sum(p["$"] for p in team if p["Name"] != removed_player["Name"])
        position = removed_player["Pos"]

        # Recommend 5 replacements
        replacements = recommend_replacements(team, removed_player["Name"], budget_left, position, players)

        # Do the swap?
        choice = choose_replacement(replacements)

        if choice == "r":
            print("Reverting to the original team.")
        else:
            print(f"Adding {replacements.iloc[int(choice)]['Name']} to the team.")
            print(f"Removed {team[removed_index]['Name']} from the team.")
            removed_player = team[removed_index]["Name"]
            replacement = replacements.iloc[int(choice)]
            team[removed_index] = {
                "Name": replacement["Name"],
                "Pos": replacement["Pos"],
                "team": replacement["team"],
                "Avg": replacement["Avg"],
                "Total Points": replacement["Total Points"],
                "$": replacement["$"],
                "Gp": replacement["Gp"],
            }
            print(f"\nAdded {replacement['Name']} to the team.")
            choice = input(
                "Do you want me to optimize team after this change? This player will be in the must include list along with any others passed as cli args.\nIt will not put the removed player back in even if it is the best team. (y/n): "
            )
            if choice.lower() == "y":
                positions_needed = {"C": 3, "W": 4, "D": 3, "G": 2}
                budget = 50
                must_include = must_include + [replacement["Name"]]
                print("Optimizing team...")
                print(f"Must include: {must_include}")
                print(f"Exclude players: {exclude_players + [removed_player]}")
                team = select_team(
                    players,
                    budget,
                    positions_needed,
                    must_include=must_include,
                    exclude_players=exclude_players + [removed_player],
                    points_type=points_type,
                )
            else:
                print("Team not optimized.")

        display_team(team)
    print(team)
    choice = input("Do you want to save the team? (y/n): ")
    if choice.lower() == "y":
        save_team_to_file(team, team_file)
    else:
        print("Team not saved.")


if __name__ == "__main__":
    main()
