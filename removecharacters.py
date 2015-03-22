"""
CHALLENGE DESCRIPTION: Write a program which removes specific characters from a string.
INPUT SAMPLE: The first argument is a path to a file. The file contains the source strings and the characters that need
to be scrubbed. Each source string and characters you need to scrub are delimited by comma.
how are you, abc
hello world, def
OUTPUT SAMPLE: Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on
each line you print.
how re you
hllo worl
"""

test_cases = {"how are you, abc", "hello world, def"}

#import sys
#test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    inputs = test.split(", ")
    string = str(inputs[0])
    removal = str(inputs[1])
    print removal
    i = 0
    for char in string:
        [removal]
    print string


#test_cases.close()
