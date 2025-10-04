Suggestions based on last years stats as to what combination gives the best points total/points per game for this years prices.

I may add this years stats as the season progresses.

*** I don't care if it doesn't work for you.

```
    Usage:
        fantasy_hockey.py [--must-include=<players>] [--exclude=<players>] [--points-type=<type>] [--minimum-games=<games>] [--budget=<budget>] [--load-team=<team>] [--replacements=<number>] [--noise]

    Options:
        --must-include=<players>  Comma-separated list of players to include.
        --exclude=<players>       Comma-separated list of players to exclude.
        --points-type=<type>      The type of points to optimize ('total' or 'average') [default: total].
        --minimum-games=<games>   Minimum number of games played [default: 40].
        --budget=<budget>         Budget for the team [default: 50].
        --load-team=<team>        Load a previously saved team from the supplied file.
        --replacements=<number>   Number of replacements to recommend [default: 20].
        --noise                   Get spammed with solver output crap.
```

Want McDavid and Bobrovsky in your team?
```
python3 fantasy_team.py --must-include="Sergei Bobrovsky,Connor McDavid"
```

Don't want Sam Reinhart and Jack Hughes in your team and want it to select your team on average points per game and played at least 30 last season:
```
python3 fantasy_team.py --exclude="Sam Reinhart,Jack Hughes" --minimum-games=30 --points-type=average
```

```
(hockey) ~/hockey_helper$ python3 fantasy_team.py --exclude='Sam Reinhart,Jack Hughes' --minimum-games=30 --points-type=average
Current Team:
  Index  name             position    team      average    matches    price    points
-------  ---------------  ----------  ------  ---------  ---------  -------  --------
      0  Sean Monahan     C           CBJ       41.2037         54  5470000      2225
      1  Sidney Crosby    C           PIT       40.725          80  5570000      3258
      2  Mathew Barzal    C           NYI       29.7333         30  3750000       892
      3  Bryan Rust       W           PIT       31.8732         71  4280000      2263
      4  Chris Kreider    W           NYR       22.6765         68  2950000      1542
      5  Adam Klapka      W           CAL       21.2581         31  2610000       659
      6  Yegor Chinakhov  W           CBJ       20.5667         30  2590000       617
      7  Zach Werenski    D           CBJ       41.3827         81  5720000      3352
      8  Quinn Hughes     D           VAN       39.3971         68  5370000      2679
      9  Sean Durzi       D           UTA       19.6667         30  2480000       590
     10  Dan Vladar       G           CAL       36.1333         30  4290000      1084
     11  Jake Allen       G           NJD       38.8387         31  4910000      1204

points: 20365.0
Total Cost: 49990000.00
Mean average PPG: 31.95
Do you want to make changes to the team? (y/n): y
Let's make some changes to the team!

Current Team:
  Index  name             position    team      average    matches    price    points
-------  ---------------  ----------  ------  ---------  ---------  -------  --------
      0  Sean Monahan     C           CBJ       41.2037         54  5470000      2225
      1  Sidney Crosby    C           PIT       40.725          80  5570000      3258
      2  Mathew Barzal    C           NYI       29.7333         30  3750000       892
      3  Bryan Rust       W           PIT       31.8732         71  4280000      2263
      4  Chris Kreider    W           NYR       22.6765         68  2950000      1542
      5  Adam Klapka      W           CAL       21.2581         31  2610000       659
      6  Yegor Chinakhov  W           CBJ       20.5667         30  2590000       617
      7  Zach Werenski    D           CBJ       41.3827         81  5720000      3352
      8  Quinn Hughes     D           VAN       39.3971         68  5370000      2679
      9  Sean Durzi       D           UTA       19.6667         30  2480000       590
     10  Dan Vladar       G           CAL       36.1333         30  4290000      1084
     11  Jake Allen       G           NJD       38.8387         31  4910000      1204

points: 20365.0
Total Cost: 49990000.00
Mean average PPG: 31.95
Enter the number of the player you want to remove: 11
Removing Jake Allen from the team.
Do you want to filter new players by team or comma separated list of teams? (y/n): y
Enter the teams you want to filter by (E.G. NYR,SEA,VAN): WSH,FLA,NYI
Do you want to include a specific player? (y/n): n

Recommended Replacements:
  Index  name              position    team      average    matches    price    points
-------  ----------------  ----------  ------  ---------  ---------  -------  --------
      0  Charlie Lindgren  G           WSH       33.1            40  4260000      1324
      1  David Rittich     G           NYI       26.4118         34  3560000       898

Enter the number of the replacement player (or type 'r' to revert): 0
Adding Charlie Lindgren to the team.
Removed Jake Allen from the team.

Added Charlie Lindgren to the team.
Do you want me to optimize team after this change? This player will be in the must include list along with any others passed as cli args.
It will not put the removed player back in even if it is the best team. (y/n): y
Optimizing team...
Must include: ['Charlie Lindgren']
Exclude players: ['Sam Reinhart', 'Jack Hughes', 'Jake Allen']
Current Team:
  Index  name              position    team      average    matches    price    points
-------  ----------------  ----------  ------  ---------  ---------  -------  --------
      0  Sean Monahan      C           CBJ       41.2037         54  5470000      2225
      1  Sidney Crosby     C           PIT       40.725          80  5570000      3258
      2  Mathew Barzal     C           NYI       29.7333         30  3750000       892
      3  Alex Tuch         W           BUF       36.378          82  4990000      2983
      4  Bryan Rust        W           PIT       31.8732         71  4280000      2263
      5  Adam Klapka       W           CAL       21.2581         31  2610000       659
      6  Yegor Chinakhov   W           CBJ       20.5667         30  2590000       617
      7  Charlie McAvoy    D           BOS       26.46           50  3480000      1323
      8  Roman Josi        D           NSH       25.1698         53  3330000      1334
      9  Quinn Hughes      D           VAN       39.3971         68  5370000      2679
     10  Dan Vladar        G           CAL       36.1333         30  4290000      1084
     11  Charlie Lindgren  G           WSH       33.1            40  4260000      1324

points: 20641.0
Total Cost: 49990000.00
Mean average PPG: 31.83
Do you want to make changes to the team? (y/n):
```




