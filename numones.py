"""NUMBER OF ONES
Write a program which determines the number of 1 bits in the internal representation of a given integer.
INPUT SAMPLE: The first argument is a path to a file. The file contains integers, one per line.
10
22
56
OUTPUT SAMPLE: Print to stdout the number of ones in the binary form of each number.
2
3
3
"""
import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = [10,22,56]
for test in test_cases:
    if test == "":
        pass
    test = int(test)
    binary = bin(test)
    total = 0
    for char in binary:
        if char.isdigit():
            if char.__eq__("1"):
                total += 1
    print total
test_cases.close()