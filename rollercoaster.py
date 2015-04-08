"""
ROLLER COASTER
CHALLENGE DESCRIPTION: You are given a piece of text. Your job is to write a program that sets the case of text
characters according to the following rules:
The first letter of the line should be in uppercase.
The next letter should be in lowercase.
The next letter should be in uppercase, and so on.
Any characters, except for the letters, are ignored during determination of letter case.
INPUT SAMPLE: The first argument will be a path to a filename containing sentences, one per line. You can assume that
all characters are from the English language.
CONSTRAINTS: The length of each piece of text does not exceed 1000 characters.
"""
import sys
test_cases = open(sys.argv[1], 'r')
lines = [line for line in test_cases]
for line in lines:
    if line == "":
        break
    counter = 0
    storage = []
    for char in line:
        if char.isalpha():
            if counter % 2 == 0:
                storage.append(char.upper())
            else:
                storage.append(char.lower())
            counter += 1
        elif char != '\n':
            storage.append(char)
    print ''.join(storage)

test_cases.close()

