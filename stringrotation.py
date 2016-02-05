"""
STRING ROTATION
CHALLENGE DESCRIPTION:
You are given two strings. Determine if the second string is a rotation of the
first string.
INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line
in this file contains two comma separated strings. E.g.
Hello,lloHe
Basefont,tBasefon
OUTPUT SAMPLE:
Print out True/False if the second string is a rotation of the first. E.g.
True
True
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    original, other = test.rstrip().split(',')
    check = False
    i = 0
    while i < len(other):
        compare = other[i:len(other)]+other[:i]
        if compare == original:
            check = True
            break
        i += 1
    print check
test_cases.close()
