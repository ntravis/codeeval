import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    nums = test.split(" ")
    first = int(nums[0])
    second = int(nums[1])
    third = int(nums[2])
    sentence = []
    for x in range(1, third+1, 1):
        if (x % first) == 0 and (x % second) == 0:
            sentence.append("FB")
        elif x % first == 0:
            sentence.append("F")
        elif x % second == 0:
            sentence.append("B")
        else:
            sentence.append(str(x))
    print ' '.join(sentence)
test_cases.close()