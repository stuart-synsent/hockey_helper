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

Want McDavid and Bobrovsky in your team in your team?
```
python3 fantasy_team.py --must-include='S Bobrovsky,C McDavid'
```

Don't want Reinhart in your team and want it to select your team on average points per game and played at least 30 last season:
```
python3 fantasy_team.py --exclude='S Reinhart' --minimum-games=30 --points-type=average
```

```
(hockey) ~/hockey_helper$ python3 fantasy_team.py --exclude='S Reinhart' --minimum-games=30 --points-type=average
Current Team:
  Index  Name        Pos    team      Avg    Gp     $    Total Points
-------  ----------  -----  ------  -----  ----  ----  --------------
      0  J Hughes    C      NJD      42.5    62  5.48            2635
      1  S Pinto     C      OTT      30.7    41  3.81            1259
      2  T Zegras    C      ANA      22.3    31  2.65             691
      3  F Vatrano   W      ANA      36.2    82  4.59            2968
      4  B Rust      W      PIT      36.6    62  4.71            2269
      5  P Kane      W      DET      34      50  4.28            1700
      6  D Guenther  W      UTA      32.8    45  4.1             1476
      7  R Gudas     D      ANA      28.3    66  3.63            1868
      8  T Chabot    D      OTT      25.3    51  3.2             1290
      9  A Xhekaj    D      MTL      22.8    44  2.85            1003
     10  I Sorokin   G      NYI      43.5    57  5.26            2480
     11  J Hofer     G      STL      44.6    30  5.43            1338

Total Points: 20977.0
Total Cost: 49.99
Mean average PPG: 33.30
Do you want to make changes to the team? (y/n): y
Let's make some changes to the team!

Enter the number of the player you want to remove: 0
Removing J Hughes from the team.
Do you want to filter new players by team or comma separated list of teams? (y/n): y
Enter the teams you want to filter by (E.G. NYR,SEA,VAN): NYR,BOS,SEA,EDM
Do you want to include a specific player? (y/n): n

Top 5 Replacements:
  Index  Name          Pos    team      Avg    Gp     $    Total Points
-------  ------------  -----  ------  -----  ----  ----  --------------
      0  C Coyle       C      BOS      29.9    95  4.83            2840
      1  P Zacha       C      BOS      29.2    91  4.64            2657
      2  A Henrique    C      EDM      27.4    99  4.53            2713
      3  E Lindholm    C      BOS      26.8    88  4.32            2358
      4  J Skinner     C      EDM      25.9    74  3.4             1917
      5  T Frederic    C      BOS      25.8    95  4.19            2451
      6  M Geekie      C      BOS      23.5    89  3.75            2092
      7  C Stephenson  C      SEA      22.7    82  3.39            1861
      8  Y Gourde      C      SEA      20.7    80  2.55            1656
      9  M Beniers     C      SEA      18.2    77  2.38            1401
     10  J Schwartz    C      SEA      18.2    62  2.36            1128
     11  M Poitras     C      BOS      18      33  2.2              594
     12  S Carrick     C      NYR      15      87  2.36            1305
     13  J Brodzinski  C      NYR      13.5    60  1.81             810
     14  M Kastelic    C      BOS      12.8    63  1.65             806
     15  M Janmark     C      EDM      12.3    96  1.99            1181
     16  J Beecher     C      BOS      11.1    64  1.71             710
     17  V Lettieri    C      BOS      10.8    46  1.35             497
     18  T Pitlick     C      NYR       8.2    34  1.01             279
     19  D Ryan        C      EDM       7.6    89  1.25             676

Enter the number of the replacement player (or type 'r' to revert): 0
Adding C Coyle to the team.
Removed J Hughes from the team.

Added C Coyle to the team.
Do you want me to optimize team after this change? This player will be in the must include list along with any others passed as cli args.
It will not put the removed player back in even if it is the best team. (y/n): n
Team not optimized.
Current Team:
  Index  Name        Pos    team      Avg    Gp     $    Total Points
-------  ----------  -----  ------  -----  ----  ----  --------------
      0  C Coyle     C      BOS      29.9    95  4.83            2840
      1  S Pinto     C      OTT      30.7    41  3.81            1259
      2  T Zegras    C      ANA      22.3    31  2.65             691
      3  F Vatrano   W      ANA      36.2    82  4.59            2968
      4  B Rust      W      PIT      36.6    62  4.71            2269
      5  P Kane      W      DET      34      50  4.28            1700
      6  D Guenther  W      UTA      32.8    45  4.1             1476
      7  R Gudas     D      ANA      28.3    66  3.63            1868
      8  T Chabot    D      OTT      25.3    51  3.2             1290
      9  A Xhekaj    D      MTL      22.8    44  2.85            1003
     10  I Sorokin   G      NYI      43.5    57  5.26            2480
     11  J Hofer     G      STL      44.6    30  5.43            1338

Total Points: 21182.0
Total Cost: 49.34
Mean average PPG: 32.25
Do you want to make changes to the team? (y/n):
```




