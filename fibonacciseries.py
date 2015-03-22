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
The first 21 Fibonacci numbers Fn for n = 0, 1, 2, ..., 20 are:[17]
F0	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F13	F14	F15	F16	F17	    F18 	F19 	F20
0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597	2584	4181	6765
"""
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break

    def fibonacci(number):
        number = int(number)
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fibonacci(number-1)+fibonacci(number-2)
            # return total

    print fibonacci(test)
test_cases.close()