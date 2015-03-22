"""
LONGEST LINES
Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based
on their length in descending order.
INPUT SAMPLE:
Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line
indicates the number of lines you should output, the other lines are of different length and are presented randomly.
You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

For example:
2
Hello World
CodeEval
Quick Fox
A
San Francisco

OUTPUT SAMPLE: Print out the longest lines limited by specified number and sorted by their length in descending order.
For example:
San Francisco
Hello World
"""
import sys
test_cases = open(sys.argv[1], 'r')
#test_cases = ["2", "Hello World", "CodeEval", "Quick Fox", "A", "San Francisco"]
overall = []
num_lines = sum(1 for line in test_cases)
#num_lines = len(test_cases)
number = 0
i = 0

for test in test_cases:
    print "gothere"
    if test == "":
        break
    elif test.isdigit():
        number = int(test)
    else:
        overall.append(test)

    if i == num_lines-1:
        overall.sort(key=len)
        overall.reverse()
        printing = 0
        while printing < number:
            print overall[printing]
            printing += 1
    i += 1
test_cases.close()