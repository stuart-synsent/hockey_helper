import pandas as pd
import pulp
import json
import tabulate
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


def select_team(players, budget, positions_needed, must_include=None, exclude_players=None, points_type="total", noise=False):
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

    couldnt_find = []
    # Include specific players
    if must_include:
        for player in must_include:
            try:
                prob += player_vars[player] == 1
                # Adjust the budget and position needed for included players
                player_row = players[players["Name"] == player].iloc[0]
                budget -= player_row["$"]
                positions_needed[player_row["Pos"]] -= 1
            except KeyError:
                print(f"Player {player} not found in the list of players.")
                couldnt_find.append(player)

    # Exclude specific players
    if exclude_players:
        for player in exclude_players:
            try:
                prob += player_vars[player] == 0
            except KeyError:
                print(f"Player {player} not found in the list of players.")
                couldnt_find.append(player)

    # and got for it!
    if noise:
        prob.solve()
    else:
        prob.solve(pulp.PULP_CBC_CMD(msg=False))

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

    if couldnt_find:
        print("****************************************************************************************************")
        print(f"Could not find the following players: {couldnt_find}")
        print("Please check the spelling and try again.")
        print("if they hadn't played the required number of games they won't be included in the list of available players.\n\n")

    return team


def recommend_replacements(
    current_team, removed_player, budget_left, position, players, num_replacements=20, team=None, specific_player=None, points_type="total"
):
    potential_replacements = players[
        (players["Name"] != removed_player)
        & (players["Pos"] == position)
        & (~players["Name"].isin([p["Name"] for p in current_team]))
        & (players["$"] <= budget_left)
    ]

    # are specific teams requested?
    if team:
        potential_replacements = potential_replacements[potential_replacements["team"].isin(team)]

    # Sort by relevant metric
    potential_replacements = potential_replacements.sort_values(by="Total Points" if points_type == "total" else "Avg", ascending=False)

    # Get the best ones.
    top_replacements = potential_replacements.head(num_replacements)

    # Check if a specific player is provided and we know about him.
    if specific_player:
        specific_player_row = players[(players["Name"] == specific_player) & (players["Pos"] == position)]

        # If the specific player exists and is not already in the top replacements and if so add to the list.
        if not specific_player_row.empty:
            if specific_player not in top_replacements["Name"].values:
                top_replacements = pd.concat([top_replacements, specific_player_row])

    return top_replacements


def display_team(team):
    position_order = {"C": 1, "W": 2, "D": 3, "G": 4}

    # Sort team by the position order
    sorted_team = sorted(team, key=lambda x: position_order[x["Pos"]])

    print("Current Team:")
    total_points = sum(player["Total Points"] for player in sorted_team)
    total_cost = sum(player["$"] for player in sorted_team)
    total_cost = "{:.2f}".format(total_cost)
    average_avg = sum(player["Avg"] for player in sorted_team) / len(sorted_team)
    average_avg = "{:.2f}".format(average_avg)
    # Add index and display the team.
    for i, player in enumerate(sorted_team):
        player['Index'] = i
    reordered_columns = ["Index", "Name", "Pos", "team", "Avg", "$", "Total Points"]
    reordered_data = [[player[col] for col in reordered_columns] for player in sorted_team]
    print(tabulate.tabulate(reordered_data, headers=reordered_columns, tablefmt="simple"))
    print(f"\nTotal Points: {total_points}")
    print(f"Total Cost: {total_cost}")
    print(f"Mean average PPG: {average_avg}")
    return sorted_team


def choose_player_to_remove(team):
    team = display_team(team)
    index = int(input("Enter the number of the player you want to remove: "))
    print(f"Removing {team[index]['Name']} from the team.")
    removed_player = team[index]
    return removed_player, index


def choose_replacement(replacements):
    replacements = replacements.to_dict('records')
    print("\nTop 5 Replacements:")
    for i, player in enumerate(replacements):
        player['Index'] = i
    reordered_columns = ["Index", "Name", "Pos", "team", "Avg", "$", "Total Points"]
    reordered_data = [[player[col] for col in reordered_columns] for player in replacements]
    print(tabulate.tabulate(reordered_data, headers=reordered_columns, tablefmt="simple"))
    choice = input("\nEnter the number of the replacement player (or type 'r' to revert): ")
    return choice


def main():
    doc = """
    Usage:
        fantasy_hockey.py [--must-include=<players>] [--exclude=<players>] [--points-type=<type>] [--minimum-games=<games>] [--budget=<budget>] [--load-team=<team>] [--noise]

    Options:
        --must-include=<players>  Comma-separated list of players to include.
        --exclude=<players>       Comma-separated list of players to exclude.
        --points-type=<type>      The type of points to optimize ('total' or 'average') [default: total].
        --minimum-games=<games>   Minimum number of games played [default: 40].
        --budget=<budget>         Budget for the team [default: 50].
        --load-team=<team>        Load a previously saved team from the supplied file.
        --noise                   Use the default solver instead of the CBC_CMD solver.
    """

    args = docopt(doc)

    must_include = args["--must-include"].split(",") if args["--must-include"] else []
    exclude_players = args["--exclude"].split(",") if args["--exclude"] else []
    points_type = args["--points-type"]
    minimum_games = int(args["--minimum-games"])
    budget = int(args["--budget"])
    noise = args["--noise"]

    file_path = "data/updated_players.csv"
    df = pd.read_csv(file_path)
    # If a required player hasn't played enough games then we'll need to save and add back.
    if must_include:
        df2 = pd.DataFrame()
        for player in must_include:
            if df[df["Name"] == player]["Gp"].values[0] < minimum_games:
                df2 = df[df["Name"] == player]

    df = df[df["Gp"] >= minimum_games]
    if must_include:
        if not df2.empty:
            df = pd.concat([df, df2])
        
    players = df[["Name", "team", "Pos", "Avg", "$", "Gp"]].copy()
    total_points = round(players["Gp"] * players["Avg"])
    players.loc[:, "Total Points"] = total_points
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
            noise=noise,
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
        player_team = input("Do you want to filter new players by team or comma separated list of teams? (y/n): ")
        if player_team.lower() == "y":
            input_team = input("Enter the teams you want to filter by (E.G. NYR,SEA,VAN): ")
            # make all caps and split by comma
            input_team = input_team.upper()
            input_team = input_team.split(",")
        else:
            input_team = None
        specific_player = input("Do you want to include a specific player? (y/n): ")
        if specific_player.lower() == "y":
            specific_player = input("Enter the name of the player you want to include (WARNING can go over budget): ")
        else:
            specific_player = None

        # Recommend 5 replacements
        replacements = recommend_replacements(team, removed_player["Name"], budget_left, position, players, team=input_team, points_type=points_type, specific_player=specific_player)

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
                    noise=noise,
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
