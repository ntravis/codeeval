"""
SUM OF INTEGERS FROM FILE
CHALLENGE DESCRIPTION: Print out the sum of integers read from a file.
INPUT SAMPLE: The first argument to the program will be a path to a filename containing a positive integer, one per line
5
12
OUTPUT SAMPLE: Print out the sum of all the integers read from the file. E.g.
17
"""
import sys
test_cases = open(sys.argv[1], 'r')
lines = [line.strip() for line in test_cases]
summing = 0
for line in lines:
    summing += int(line)
print summing
test_cases.close()