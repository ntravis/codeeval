"""
MULTIPLES OF A NUMBER
CHALLENGE DESCRIPTION: Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is
greater than or equal to x. Do not use division or modulo operator.
INPUT SAMPLE: The first argument will be a path to a filename containing a comma separated list of two integers, one
list per line. E.g.
13,8
17,16
OUTPUT SAMPLE: Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.
16
32
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    nums = test.split(",")
    x = int(nums[0])
    n = int(nums[1])
    while x > n:
        n **= 2
    print n
test_cases.close()