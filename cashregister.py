"""
CASH REGISTER
CHALLENGE DESCRIPTION: The goal of this challenge is to design a cash register program. You will be given two float
numbers. The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer. Your
register currently has the following bills/coins within it:

'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00

The aim of the program is to calculate the change that has to be returned to the customer.
INPUT SAMPLE: Your program should accept as its first argument a path to a filename. The input file contains several
lines. Each line is one test case. Each line contains two numbers which are separated by a semicolon. The first is the
Purchase price (PP) and the second is the cash(CH) given by the customer. eg.
15.94;16.00
17;16
35;35
45;50
OUTPUT SAMPLE: For each set of input produce a single line of output which is the change to be returned to the customer.
In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be
returned, in terms of the currency values provided. The output should be sorted in highest-to-lowest order (DIME,NICKEL,
PENNY). eg.
NICKEL,PENNY
ERROR
ZERO
FIVE
"""

import sys
test_cases = open(sys.argv[1], 'r')
register = {
    'PENNY': .01,
    'NICKEL': .05,
    'DIME': .10,
    'QUARTER': .25,
    'HALF DOLLAR': .50,
    'ONE': 1.00,
    'TWO': 2.00,
    'FIVE': 5.00,
    'TEN': 10.00,
    'TWENTY': 20.00,
    'FIFTY': 50.00,
    'ONE HUNDRED': 100.00
}
for test in test_cases:
    if test == "":
        break
    price = float(test.split(";")[0])
    # 15.94
    cash = float(test.split(";")[1])
    # 16.00
    if price == cash:
        print "ZERO"
    elif price > cash:
        print "ERROR"
    else:
        change = []
        # while 15.94 + 0 != 16
        while price + sum(change) != cash:
            # what do we need to make change for right now?
            difference = cash - (price + sum(change))
            # difference = .06
            # find the highest value of register that is less than the difference?
            x = 0.0
            current = 0.0
            while x < difference:
                for value in register.itervalues():
                    x = value
                
test_cases.close()
