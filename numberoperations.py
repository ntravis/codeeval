"""
NUMBER OPERATIONS
CHALLENGE DESCRIPTION: Alice has invented a new card game to play with Bob. Alice made a deck of cards with random
values between 1 and 52. Bob picks 5 cards. Then, he has to rearrange the cards so that by utilizing the operations plus,
minus, or times, the value of the cards reach Alice's favorite number, 42. More precisely, find operations such that
((((val1 op1 val2) op2 val3) op3 val4) op4 val5) = 42.

Help Bob by writing a program to determine whether it is possible to reach 42 given 5 card values.
For example, Bob picks 5 cards out of the deck containing 60, 1, 3, 5, and 20. Bob rearranges the cards and supplies four
operations, so that 5 * 20 - 60 + 3 - 1 = 42.
INPUT SAMPLE: The input consists of five integers on a line, separated by spaces. Each integer V is 0 <= V <= 52.
44 6 1 49 47
34 1 49 2 21
31 38 27 51 18
OUTPUT SAMPLE: For each test case print a line containing "YES" if it is possible to reach the value 42 according to the
rules of the game, or "NO" otherwise.
NO
YES
NO
"""
import operator
ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul}
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test == "":
        break
    numbers = test.strip().split(" ")
    for op1 in ops:
        op1_func = ops[op1]
        for op2 in ops:
            op2_func = ops[op2]
            for op3 in ops:
                op3_func = ops[op3]
                for op4 in ops:
                    op4_func = ops[op4]
                    result = int(op4_func(int(op3_func(int(op2_func(int(op1_func(numbers[0], numbers[1])), numbers[2])), numbers[3])), numbers[4]))
                    if result == 42:
                        print "YES"
                    else:
                        print "NO"
test_cases.close()
