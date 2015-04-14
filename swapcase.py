"""
SWAP CASE
CHALLENGE DESCRIPTION: Write a program which swaps letters' case in a sentence. All non-letter characters should remain
the same.
INPUT SAMPLE: Your program should accept as its first argument a path to a filename. Input example is the following
Hello world!
JavaScript language 1.8
A letter
OUTPUT SAMPLE: Print results in the following way.
hELLO WORLD!
jAVAsCRIPT LANGUAGE 1.8
a LETTER
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
            if char.islower():
                storage.append(char.upper())
            else:
                storage.append(char.lower())
            counter += 1
        elif char != '\n':
            storage.append(char)
    print ''.join(storage)

test_cases.close()

