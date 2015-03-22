"""RIGHTMOST CHAR
You are given a string 'S' and a character 't'. Print out the position of the rightmost occurrence of 't' (case matters)
 in 'S' or -1 if there is none. The position to be printed out is zero based.
INPUT SAMPLE:
The first argument will ba a path to a filename, containing a string and a character, comma delimited, one per line.
Ignore all empty lines in the input file. E.g.
Hello World,r
Hello CodeEval,E
OUTPUT SAMPLE:
Print out the zero based position of the character 't' in string 'S', one per line. Do NOT print out empty lines between
your output.
8
10
"""
#import sys
#test_cases = open(sys.argv[1], 'r')
test_cases = {"Hello World,r", "Hello CodeEval,E", "Test Number,x","zzx z,z"}

for test in test_cases:
    if test == "":
        break
    strings = test.split(",")
    string = strings[0]
    char = strings[1]
    print string
    print char

    i = 0
    location = -1

    for letter in string:
        if letter == char:
            location = i
        i += 1
    print location
#test_cases.close()