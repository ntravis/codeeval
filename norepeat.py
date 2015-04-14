"""
FIRST NON-REPEATED CHARACTER
CHALLENGE DESCRIPTION: Write a program which finds the first non-repeated character in a string.
INPUT SAMPLE: The first argument is a path to a file. The file contains strings. For example:
yellow
tooth
OUTPUT SAMPLE: Print to stdout the first non-repeated character, one per line. For example:
y
h
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    for char in test:
        if test.count(char) == 1:
            print char
            break
test_cases.close()
