"""
MINIMUM COINS
CHALLENGE DESCRIPTION: You are given 3 coins of value 1, 3 and 5. You are also given a total which you have to arrive
 at. Find the minimum number of coins to arrive at it.
INPUT SAMPLE: Your program should accept as its first argument a path to a filename. Each line in this file contains a
positive integer number which represents the total you have to arrive at. E.g.
11
20
OUTPUT SAMPLE: Print out the minimum number of coins required to arrive at the total.
3
4
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        pass
    else:
        total = int(test)
        leftover = total % 5
        coins = 0
        running = 0

test_cases.close()