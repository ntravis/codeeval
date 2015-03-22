"""MTH TO LAST ELEMENT
CHALLENGE DESCRIPTION: Write a program which determines the Mth to the last element in a list.
INPUT SAMPLE: The first argument is a path to a file. The file contains the series of space delimited characters
followed by an integer. The integer represents an index in the list (1-based), one per line.
a b c d 4
e f g h 2
OUTPUT SAMPLE: Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the
number of elements in the list, ignore that input.
a
g
"""
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        pass
    else:
        overall = test.split(" ")
        printing = int(overall[len(overall)-1])-1
        overall.pop(len(overall)-1)
        overall.reverse()
        print overall[printing]
test_cases.close()