# coding=utf-8
# coding=utf-8
"""
The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0,
print out the F(n).
INPUT SAMPLE:
The first argument will be a path to a filename containing integer numbers, one per line. E.g.
5
12
OUTPUT SAMPLE:
Print to stdout, the fibonacci number, F(n). E.g.
5
144
Sample code to read in test cases:
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
test_cases.close()
"""
# import sys
# test_cases = open(sys.argv[1], 'r')
test_cases = {18, 9, 11, 1, 12, 15, 10, 14, 19, 17, 0, 7, 4, 16, 3, 6, 13, 5, 2, 8}
for test in test_cases:
    if test == "":
        break
# test_cases.close()