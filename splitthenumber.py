"""
CHALLENGE DESCRIPTION:
You are given a number N and a pattern. The pattern consists of lowercase latin letters and one operation "+" or "-".
The challenge is to split the number and evaluate it according to this pattern e.g.
1232 ab+cd -> a:1, b:2, c:3, d:2 -> 12+32 -> 44
INPUT SAMPLE:
Your program should accept as its first argument a path to a filename. Each line of the file is a test case, containing
the number and the pattern separated by a single whitespace. E.g.
3413289830 a-bcdefghij
776 a+bc
12345 a+bcde
1232 ab+cd
90602 a+bcde

OUTPUT SAMPLE:
For each test case print out the result of pattern evaluation. E.g.
-413289827
83
2346
44
611
90602 a+bcde= 611
Constraints:
N is in range [100, 1000000000]
"""

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    parts = test.split()
    pattern = parts[1]
    numbers = parts[0]
    i = 0
    for letter in pattern:
        if pattern[i] == "+" or pattern[i] == "-":
            operator = pattern[i]
            first = numbers[:i]
            last = numbers[i:]
        i += 1
    if operator == "+":
        print int(first)+int(last)
    else:
        print int(first)-int(last)
test_cases.close()
