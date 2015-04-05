"""
URI COMPARISON
CHALLENGE DESCRIPTION: Determine if two URIs match. For the purpose of this challenge, you should use a case-sensitive
octet-by-octet comparison of the entire URIs, with these exceptions:
1. A port that is empty or not given is equivalent to the default port of 80
2. Comparisons of host names MUST be case-insensitive
3. Comparisons of scheme names MUST be case-insensitive
4. Characters are equivalent to their % HEX HEX encodings. (Other than typical reserved characters in urls
like , / ? : @ & = + $ #)
INPUT SAMPLE: Your program should accept as its first argument a path to a filename. Each line in this file contains
two urls delimited by a semicolon. E.g.
http://abc.com:80/~smith/home.html;http://ABC.com/%7Esmith/home.html
OUTPUT SAMPLE: Print out True/False if the URIs match. E.g.
True
"""
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    urls = test.split(";")
    uri1 = urls[0].lower().split("/")
    uri2 = urls[1].lower().split("/")
    iterator = 0
    check = True
    for x in uri1:
        print str(uri1[iterator]) +" " + str(uri2[iterator])
        print uri1[iterator] != uri2[iterator]
        if uri1[iterator] != uri2[iterator]:
            check = False
        iterator += 1
    print check
test_cases.close()
