"""
STACK IMPLEMENTATION
CHALLENGE DESCRIPTION: Write a program which implements a stack interface for integers. The interface should have ‘push’
and ‘pop’ functions. Your task is to ‘push’ a series of integers and then ‘pop’ and print every alternate integer.
INPUT SAMPLE: Your program should accept a file as its first argument. The file contains a series of space delimited
integers, one per line.
1 2 3 4
10 -2 3 4
OUTPUT SAMPLE: Print to stdout every alternate space delimited integer, one per line.
4 2
4 -2

"""


def push(toappend, x):
    toappend.append(x)
    return toappend


def pop(jump):
    print ' '.join(jump[:2:-1])

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    overall = []
    if test == "":
        break
    ints = test.split(" ")
    for i in ints:
        overall = push(overall, int(i))
    pop(overall)
test_cases.close()
