"""
MULTIPLICATION TABLES
CHALLENGE DESCRIPTION: Print out the grade school multiplication table up to 12*12.
OUTPUT SAMPLE: Print out the table in a matrix like fashion, each number formatted to a width of 4 (The numbers are
right-aligned and strip out leading/trailing spaces on each line). The first 3 line will look like:

1   2   3   4   5   6   7   8   9  10  11  12
2   4   6   8  10  12  14  16  18  20  22  24
3   6   9  12  15  18  21  24  27  30  33  36
"""
x = 1
y = 1
while y <= 12:
    row = ""
    while x <= 12:
        total = str(x * y)
        while len(total) < 4:
            total = ' ' + total
        row += total
        x += 1
    print row
    x = 1
    y += 1