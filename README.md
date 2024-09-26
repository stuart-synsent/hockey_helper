```
    Usage:
        fantasy_hockey.py [--must-include=<players>] [--exclude=<players>] [--points-type=<type>] [--minimum-games=<games>] [--budget=<budget>] [--load-team=<team>]

    Options:
        --must-include=<players>  Comma-separated list of players to include.
        --exclude=<players>       Comma-separated list of players to exclude.
        --points-type=<type>      The type of points to optimize ('total' or 'average') [default: total].
        --minimum-games=<games>   Minimum number of games played [default: 40].
        --budget=<budget>         Budget for the team [default: 50].
        --load-team=<team>        Load a previously saved team from the supplied file.
```


```
$ python3 fantasy_team.py

Welcome to the CBC MILP Solver
Version: 2.10.3
Build Date: Dec 15 2019


At line 2 NAME          MODEL
At line 3 ROWS
At line 10 COLUMNS
At line 3266 RHS
At line 3272 BOUNDS
At line 3924 ENDATA
Problem MODEL has 5 rows, 651 columns and 1302 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 30216.1 - 0.00 seconds
Cgl0004I processed model has 5 rows, 650 columns (650 integer (650 of which binary)) and 1300 elements
Cutoff increment increased from 1e-05 to 0.9999
Cbc0038I Initial state - 2 integers unsatisfied sum - 0.668142
Cbc0038I Solution found of -29287
Cbc0038I Before mini branch and bound, 648 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 650 columns, reduced to 0 rows 0 columns
Cbc0038I Mini branch and bound did not improve solution (0.01 seconds)
Cbc0038I Round again with cutoff of -29380.8
Cbc0038I Reduced cost fixing fixed 21 variables on major pass 2
Cbc0038I Pass   1: suminf.    0.03878 (2) obj. -29380.8 iterations 6
Cbc0038I Pass   2: suminf.    0.65554 (2) obj. -29935 iterations 6
Cbc0038I Pass   3: suminf.    0.47772 (2) obj. -29380.8 iterations 5
Cbc0038I Pass   4: suminf.    0.99778 (4) obj. -29380.8 iterations 27
Cbc0038I Pass   5: suminf.    0.96504 (3) obj. -29380.8 iterations 3
Cbc0038I Pass   6: suminf.    0.24046 (4) obj. -29380.8 iterations 6
Cbc0038I Pass   7: suminf.    0.15680 (3) obj. -29380.8 iterations 2
Cbc0038I Pass   8: suminf.    0.92783 (3) obj. -29380.8 iterations 7
Cbc0038I Pass   9: suminf.    0.27995 (2) obj. -29445.8 iterations 5
Cbc0038I Pass  10: suminf.    0.84406 (3) obj. -29380.8 iterations 5
Cbc0038I Pass  11: suminf.    1.38024 (4) obj. -29380.8 iterations 20
Cbc0038I Pass  12: suminf.    0.72510 (3) obj. -29380.8 iterations 6
Cbc0038I Pass  13: suminf.    0.52811 (2) obj. -29380.8 iterations 7
Cbc0038I Solution found of -29516
Cbc0038I Before mini branch and bound, 621 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 650 columns, reduced to 5 rows 28 columns
Cbc0038I Mini branch and bound improved solution from -29516 to -30175 (0.01 seconds)
Cbc0038I Round again with cutoff of -30184
Cbc0038I Reduced cost fixing fixed 583 variables on major pass 3
Cbc0038I Pass  14: suminf.    0.64510 (2) obj. -30184 iterations 4
Cbc0038I Pass  15: suminf.    0.96166 (2) obj. -30214.4 iterations 5
Cbc0038I Pass  16: suminf.    0.97743 (2) obj. -30184 iterations 4
Cbc0038I Pass  17: suminf.    0.18495 (3) obj. -30184 iterations 8
Cbc0038I Pass  18: suminf.    0.13255 (2) obj. -30185 iterations 4
Cbc0038I Pass  19: suminf.    0.13304 (2) obj. -30184 iterations 4
Cbc0038I Pass  20: suminf.    0.87868 (4) obj. -30184 iterations 8
Cbc0038I Pass  21: suminf.    0.40591 (4) obj. -30184 iterations 4
Cbc0038I Pass  22: suminf.    0.56259 (2) obj. -30194.8 iterations 5
Cbc0038I Pass  23: suminf.    0.55747 (2) obj. -30184 iterations 4
Cbc0038I Pass  24: suminf.    0.23003 (2) obj. -30186.6 iterations 8
Cbc0038I Pass  25: suminf.    0.23003 (2) obj. -30186.6 iterations 3
Cbc0038I Pass  26: suminf.    0.37434 (2) obj. -30184 iterations 5
Cbc0038I Pass  27: suminf.    0.36819 (2) obj. -30196.9 iterations 4
Cbc0038I Pass  28: suminf.    0.38461 (4) obj. -30184 iterations 10
Cbc0038I Pass  29: suminf.    0.33082 (3) obj. -30184 iterations 4
Cbc0038I Pass  30: suminf.    0.45766 (4) obj. -30184 iterations 5
Cbc0038I Pass  31: suminf.    1.36199 (4) obj. -30184 iterations 9
Cbc0038I Pass  32: suminf.    0.67747 (2) obj. -30190.4 iterations 3
Cbc0038I Pass  33: suminf.    0.68049 (2) obj. -30184 iterations 4
Cbc0038I Pass  34: suminf.    0.53575 (3) obj. -30184 iterations 9
Cbc0038I Pass  35: suminf.    0.31517 (2) obj. -30188.1 iterations 4
Cbc0038I Pass  36: suminf.    0.31711 (2) obj. -30184 iterations 4
Cbc0038I Pass  37: suminf.    0.62985 (4) obj. -30184 iterations 8
Cbc0038I Pass  38: suminf.    0.39470 (2) obj. -30185.3 iterations 3
Cbc0038I Pass  39: suminf.    0.39532 (2) obj. -30184 iterations 4
Cbc0038I Pass  40: suminf.    1.00000 (3) obj. -30184 iterations 7
Cbc0038I Pass  41: suminf.    1.00000 (3) obj. -30184 iterations 8
Cbc0038I Pass  42: suminf.    0.78980 (2) obj. -30184 iterations 2
Cbc0038I Pass  43: suminf.    0.28068 (2) obj. -30184 iterations 5
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 623 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 650 columns, reduced to 4 rows 26 columns
Cbc0038I Mini branch and bound improved solution from -30175 to -30198 (0.02 seconds)
Cbc0038I Round again with cutoff of -30204.1
Cbc0038I Reduced cost fixing fixed 626 variables on major pass 4
Cbc0038I Pass  43: suminf.    0.65956 (2) obj. -30204.1 iterations 0
Cbc0038I Pass  44: suminf.    0.96166 (2) obj. -30214.4 iterations 4
Cbc0038I Pass  45: suminf.    0.96700 (2) obj. -30204.1 iterations 3
Cbc0038I Pass  46: suminf.    0.71300 (4) obj. -30204.1 iterations 5
Cbc0038I Pass  47: suminf.    0.71300 (4) obj. -30204.1 iterations 0
Cbc0038I Pass  48: suminf.    0.55385 (2) obj. -30205.4 iterations 3
Cbc0038I Pass  49: suminf.    0.12880 (2) obj. -30206.1 iterations 2
Cbc0038I Pass  50: suminf.    0.91878 (4) obj. -30204.1 iterations 5
Cbc0038I Pass  51: suminf.    0.40253 (3) obj. -30204.1 iterations 2
Cbc0038I Pass  52: suminf.    0.98687 (2) obj. -30204.1 iterations 5
Cbc0038I Pass  53: suminf.    0.98390 (2) obj. -30209.2 iterations 3
Cbc0038I Pass  54: suminf.    0.98687 (2) obj. -30204.1 iterations 3
Cbc0038I Pass  55: suminf.    1.72709 (4) obj. -30204.1 iterations 7
Cbc0038I Pass  56: suminf.    0.12880 (2) obj. -30206.1 iterations 3
Cbc0038I Pass  57: suminf.    0.91878 (4) obj. -30204.1 iterations 5
Cbc0038I Pass  58: suminf.    0.40253 (3) obj. -30204.1 iterations 2
Cbc0038I Pass  59: suminf.    0.98687 (2) obj. -30204.1 iterations 5
Cbc0038I Pass  60: suminf.    0.98390 (2) obj. -30209.2 iterations 3
Cbc0038I Pass  61: suminf.    0.98687 (2) obj. -30204.1 iterations 3
Cbc0038I Pass  62: suminf.    0.77975 (2) obj. -30204.1 iterations 3
Cbc0038I Pass  63: suminf.    0.77975 (2) obj. -30204.1 iterations 3
Cbc0038I Pass  64: suminf.    0.77996 (2) obj. -30204.5 iterations 5
Cbc0038I Pass  65: suminf.    0.77975 (2) obj. -30204.1 iterations 4
Cbc0038I Pass  66: suminf.    0.85917 (4) obj. -30204.1 iterations 7
Cbc0038I Pass  67: suminf.    0.71300 (4) obj. -30204.1 iterations 3
Cbc0038I Pass  68: suminf.    0.96700 (2) obj. -30204.1 iterations 4
Cbc0038I Pass  69: suminf.    0.96166 (2) obj. -30214.4 iterations 3
Cbc0038I Pass  70: suminf.    0.43928 (2) obj. -30211.5 iterations 4
Cbc0038I Pass  71: suminf.    0.39367 (2) obj. -30204.1 iterations 3
Cbc0038I Pass  72: suminf.    0.77996 (2) obj. -30204.5 iterations 4
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 641 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 650 columns, reduced to 3 rows 9 columns
Cbc0038I Mini branch and bound did not improve solution (0.03 seconds)
Cbc0038I After 0.03 seconds - Feasibility pump exiting with objective of -30198 - took 0.02 seconds
Cbc0012I Integer solution of -30198 found by feasibility pump after 0 iterations and 0 nodes (0.03 seconds)
Cbc0038I Full problem 5 rows 650 columns, reduced to 2 rows 6 columns
Cbc0031I 2 added rows had average density of 6
Cbc0013I At root node, 2 cuts changed objective from -30216.051 to -30215.69 in 3 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 1 (Gomory) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 2 row cuts average 6.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0010I After 0 nodes, 1 on tree, -30198 best solution, best possible -30215.69 (0.03 seconds)
Cbc0001I Search completed - best objective -30198, took 61 iterations and 12 nodes (0.04 seconds)
Cbc0032I Strong branching done 50 times (98 iterations), fathomed 4 nodes and fixed 2 variables
Cbc0035I Maximum depth 3, 675 variables fixed on reduced cost
Cuts at root node changed objective from -30216.1 to -30215.7
Probing was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Gomory was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Knapsack was tried 21 times and created 13 cuts of which 0 were active after adding rounds of cuts (0.003 seconds)
Clique was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
FlowCover was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)

Result - Optimal solution found

Objective value:                30198.00000000
Enumerated nodes:               12
Total iterations:               61
Time (CPU seconds):             0.04
Time (Wallclock seconds):       0.04

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.04   (Wallclock seconds):       0.04

Current Team:
 0. L Draisaitl     - C - EDM - 50.4 PPG -  8.65 cost - Total Points: 5342.0
 1. S Reinhart      - C - FLA - 47.0 PPG -  7.93 cost - Total Points: 4982.0
 2. Y Gourde        - C - SEA - 20.7 PPG -  2.55 cost - Total Points: 1656.0
 3. F Vatrano       - W - ANA - 36.2 PPG -  4.59 cost - Total Points: 2968.0
 4. O Bjorkstrand   - W - SEA - 24.6 PPG -   3.2 cost - Total Points: 2017.0
 5. M MacCelli      - W - UTA - 22.7 PPG -  3.02 cost - Total Points: 1861.0
 6. A Holtz         - W - VGK - 12.4 PPG -  1.65 cost - Total Points: 1017.0
 7. E Bouchard      - D - EDM - 47.0 PPG -  7.97 cost - Total Points: 4982.0
 8. N Mikkola       - D - FLA - 18.7 PPG -  3.15 cost - Total Points: 1982.0
 9. J Oleksiak      - D - SEA - 14.8 PPG -   1.9 cost - Total Points: 1214.0
10. J Korpisalo     - G - BOS - 24.7 PPG -  3.15 cost - Total Points: 1358.0
11. J Gibson        - G - ANA - 17.8 PPG -  2.23 cost - Total Points:  819.0

Total Points: 30198.0
Total Cost: 49.99
Do you want to make changes to the team? (y/n): y
Let's make some changes to the team!

Enter the number of the player you want to remove: 0
Removing L Draisaitl from the team.

Top 5 Replacements:
 0. J Miller        - C - VAN - 53.1 PPG -   8.5 cost - Total Points: 4991.0
 1. V Trocheck      - C - NYR - 44.4 PPG -  7.31 cost - Total Points: 4351.0
 2. A Barkov        - C - FLA - 43.3 PPG -  7.29 cost - Total Points: 4200.0
 3. S Aho           - C - CAR - 46.7 PPG -  7.39 cost - Total Points: 4156.0
 4. E Pettersson    - C - VAN - 41.4 PPG -  6.63 cost - Total Points: 3933.0

Enter the number of the replacement player (or type 'r' to revert): 1
Adding V Trocheck to the team.
Removed L Draisaitl from the team.

Added V Trocheck to the team.
Do you want me to optimize team after this change? This player will be in the must include list along with any others passed as cli args.
It will not put the removed player back in even if it is the best team. (y/n): y
Optimizing team...
Must include: ['V Trocheck']
Exclude players: ['L Draisaitl']
Welcome to the CBC MILP Solver
Version: 2.10.3
Build Date: Dec 15 2019

At line 2 NAME          MODEL
At line 3 ROWS
At line 12 COLUMNS
At line 3270 RHS
At line 3278 BOUNDS
At line 3930 ENDATA
Problem MODEL has 7 rows, 651 columns and 1304 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 30042.7 - 0.00 seconds
Cgl0002I 1 variables fixed
Cgl0004I processed model has 5 rows, 648 columns (648 integer (648 of which binary)) and 1296 elements
Cutoff increment increased from 1e-05 to 0.9999
Cbc0038I Initial state - 2 integers unsatisfied sum - 0.37931
Cbc0038I Solution found of -29839
Cbc0038I Before mini branch and bound, 646 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 648 columns, reduced to 0 rows 0 columns
Cbc0038I Mini branch and bound did not improve solution (0.01 seconds)
Cbc0038I Round again with cutoff of -29860.3
Cbc0038I Reduced cost fixing fixed 404 variables on major pass 2
Cbc0038I Pass   1: suminf.    0.01093 (2) obj. -29860.3 iterations 4
Cbc0038I Pass   2: suminf.    0.34362 (2) obj. -29879.3 iterations 6
Cbc0038I Pass   3: suminf.    0.33546 (2) obj. -29860.3 iterations 4
Cbc0038I Pass   4: suminf.    1.52539 (4) obj. -29860.3 iterations 23
Cbc0038I Pass   5: suminf.    1.30474 (4) obj. -29860.3 iterations 1
Cbc0038I Pass   6: suminf.    0.12796 (2) obj. -29967.4 iterations 6
Cbc0038I Pass   7: suminf.    0.17559 (2) obj. -29860.3 iterations 4
Cbc0038I Pass   8: suminf.    1.09969 (4) obj. -29860.3 iterations 11
Cbc0038I Pass   9: suminf.    0.25452 (2) obj. -29860.3 iterations 6
Cbc0038I Pass  10: suminf.    0.71488 (2) obj. -29874.1 iterations 10
Cbc0038I Pass  11: suminf.    0.70875 (2) obj. -29860.3 iterations 7
Cbc0038I Pass  12: suminf.    0.88904 (3) obj. -29860.3 iterations 14
Cbc0038I Pass  13: suminf.    0.52236 (2) obj. -29860.3 iterations 4
Cbc0038I Pass  14: suminf.    0.52851 (2) obj. -29874.1 iterations 4
Cbc0038I Pass  15: suminf.    0.86305 (4) obj. -29860.3 iterations 12
Cbc0038I Pass  16: suminf.    0.20958 (2) obj. -29872.8 iterations 5
Cbc0038I Pass  17: suminf.    0.21539 (2) obj. -29860.3 iterations 4
Cbc0038I Pass  18: suminf.    0.43398 (3) obj. -29860.3 iterations 10
Cbc0038I Pass  19: suminf.    0.05962 (2) obj. -29860.3 iterations 5
Cbc0038I Pass  20: suminf.    0.62096 (3) obj. -29860.3 iterations 11
Cbc0038I Pass  21: suminf.    0.40844 (3) obj. -29860.3 iterations 5
Cbc0038I Pass  22: suminf.    1.00000 (3) obj. -29860.3 iterations 6
Cbc0038I Pass  23: suminf.    0.48639 (3) obj. -29860.3 iterations 8
Cbc0038I Pass  24: suminf.    0.11792 (2) obj. -29860.3 iterations 5
Cbc0038I Pass  25: suminf.    0.62096 (3) obj. -29860.3 iterations 11
Cbc0038I Pass  26: suminf.    0.40844 (3) obj. -29860.3 iterations 5
Cbc0038I Pass  27: suminf.    1.00000 (3) obj. -29860.3 iterations 6
Cbc0038I Pass  28: suminf.    0.48639 (3) obj. -29860.3 iterations 8
Cbc0038I Pass  29: suminf.    0.11792 (2) obj. -29860.3 iterations 5
Cbc0038I Pass  30: suminf.    0.62096 (3) obj. -29860.3 iterations 11
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 613 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 648 columns, reduced to 4 rows 35 columns
Cbc0038I Mini branch and bound improved solution from -29839 to -30035 (0.02 seconds)
Cbc0038I Round again with cutoff of -30037.3
Cbc0038I Reduced cost fixing fixed 633 variables on major pass 3
Cbc0038I Pass  30: suminf.    0.19745 (2) obj. -30037.3 iterations 1
Cbc0038I Pass  31: suminf.    0.20245 (2) obj. -30042.4 iterations 4
Cbc0038I Pass  32: suminf.    0.19745 (2) obj. -30037.3 iterations 3
Cbc0038I Pass  33: suminf.    0.20245 (2) obj. -30042.4 iterations 3
Cbc0038I Pass  34: suminf.    0.71261 (2) obj. -30037.3 iterations 6
Cbc0038I Pass  35: suminf.    0.58172 (2) obj. -30037.3 iterations 2
Cbc0038I Pass  36: suminf.    0.58282 (2) obj. -30038.4 iterations 3
Cbc0038I Pass  37: suminf.    0.58172 (2) obj. -30037.3 iterations 3
Cbc0038I Pass  38: suminf.    0.82662 (2) obj. -30037.3 iterations 6
Cbc0038I Pass  39: suminf.    0.82662 (2) obj. -30037.3 iterations 0
Cbc0038I Pass  40: suminf.    0.82822 (2) obj. -30038.9 iterations 3
Cbc0038I Pass  41: suminf.    0.61314 (2) obj. -30038.3 iterations 2
Cbc0038I Pass  42: suminf.    0.47458 (2) obj. -30038.4 iterations 1
Cbc0038I Pass  43: suminf.    0.90805 (2) obj. -30039.4 iterations 2
Cbc0038I Pass  44: suminf.    0.90805 (2) obj. -30039.4 iterations 0
Cbc0038I Pass  45: suminf.    0.58172 (2) obj. -30037.3 iterations 4
Cbc0038I Pass  46: suminf.    0.58282 (2) obj. -30038.4 iterations 3
Cbc0038I Pass  47: suminf.    0.50000 (2) obj. -30041.5 iterations 5
Cbc0038I Pass  48: suminf.    0.09205 (2) obj. -30041.1 iterations 2
Cbc0038I Pass  49: suminf.    0.60195 (2) obj. -30037.3 iterations 4
Cbc0038I Pass  50: suminf.    0.60123 (2) obj. -30038.1 iterations 3
Cbc0038I Pass  51: suminf.    0.79498 (2) obj. -30039.7 iterations 4
Cbc0038I Pass  52: suminf.    0.58172 (2) obj. -30037.3 iterations 4
Cbc0038I Pass  53: suminf.    0.58282 (2) obj. -30038.4 iterations 3
Cbc0038I Pass  54: suminf.    0.75862 (2) obj. -30041.2 iterations 4
Cbc0038I Pass  55: suminf.    0.19745 (2) obj. -30037.3 iterations 3
Cbc0038I Pass  56: suminf.    0.20245 (2) obj. -30042.4 iterations 3
Cbc0038I Pass  57: suminf.    0.50000 (2) obj. -30041.5 iterations 2
Cbc0038I Pass  58: suminf.    0.09205 (2) obj. -30041.1 iterations 2
Cbc0038I Pass  59: suminf.    0.60195 (2) obj. -30037.3 iterations 4
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 640 integers at bound fixed and 0 continuous
Cbc0038I Full problem 5 rows 648 columns, reduced to 2 rows 8 columns
Cbc0038I Mini branch and bound did not improve solution (0.02 seconds)
Cbc0038I After 0.02 seconds - Feasibility pump exiting with objective of -30035 - took 0.02 seconds
Cbc0012I Integer solution of -30035 found by feasibility pump after 0 iterations and 0 nodes (0.02 seconds)
Cbc0038I Full problem 5 rows 648 columns, reduced to 2 rows 3 columns
Cbc0006I The LP relaxation is infeasible or too expensive
Cbc0031I 4 added rows had average density of 6
Cbc0013I At root node, 4 cuts changed objective from -30042.69 to -30039.909 in 3 passes
Cbc0014I Cut generator 0 (Probing) - 7 row cuts average 4.3 elements, 6 column cuts (6 active)  in 0.000 seconds - new frequency is 1
Cbc0014I Cut generator 1 (Gomory) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 2 row cuts average 6.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0001I Search completed - best objective -30035, took 6 iterations and 0 nodes (0.03 seconds)
Cbc0035I Maximum depth 0, 632 variables fixed on reduced cost
Cuts at root node changed objective from -30042.7 to -30039.9
Probing was tried 3 times and created 13 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Gomory was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Knapsack was tried 2 times and created 2 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Clique was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
FlowCover was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)

Result - Optimal solution found

Objective value:                30035.00000000
Enumerated nodes:               0
Total iterations:               6
Time (CPU seconds):             0.02
Time (Wallclock seconds):       0.03

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.02   (Wallclock seconds):       0.03

Current Team:
 0. S Reinhart      - C - FLA - 47.0 PPG -  7.93 cost - Total Points: 4982.0
 1. V Trocheck      - C - NYR - 44.4 PPG -  7.31 cost - Total Points: 4351.0
 2. Y Gourde        - C - SEA - 20.7 PPG -  2.55 cost - Total Points: 1656.0
 3. F Vatrano       - W - ANA - 36.2 PPG -  4.59 cost - Total Points: 2968.0
 4. J Slafkovsky    - W - MTL - 25.5 PPG -  3.39 cost - Total Points: 2091.0
 5. O Bjorkstrand   - W - SEA - 24.6 PPG -   3.2 cost - Total Points: 2017.0
 6. B Saad          - W - STL - 19.7 PPG -  2.63 cost - Total Points: 1615.0
 7. E Bouchard      - D - EDM - 47.0 PPG -  7.97 cost - Total Points: 4982.0
 8. N Mikkola       - D - FLA - 18.7 PPG -  3.15 cost - Total Points: 1982.0
 9. J Oleksiak      - D - SEA - 14.8 PPG -   1.9 cost - Total Points: 1214.0
10. J Korpisalo     - G - BOS - 24.7 PPG -  3.15 cost - Total Points: 1358.0
11. J Gibson        - G - ANA - 17.8 PPG -  2.23 cost - Total Points:  819.0

Total Points: 30035.0
Total Cost: 50.00
Do you want to make changes to the team? (y/n):

```
