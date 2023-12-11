import sys


# checks spaces around point and returns the list of numbers
def checkAround(row, col):
    numbers = []
    # loops through all adjacent spaces
    for c in range(-1, 2, 1):
        i = 1 if c**2 == 1 else 2
        for r in range(-1, 2, i):
            if info[row + r][col + c].isdigit():
                appendNumber(numbers, row + r, col + c, r, c)
    return numbers


# makes sure we are appending a new number rather than a same one
def appendNumber(numbers, row, col, r, c):
    if r == 0 or c == -1 or not info[row][col - 1].isdigit():
        numbers.append(findNumber(row, col))


# returns the number associated with a position
def findNumber(row, col):
    number = ""
    while info[row][col - 1].isdigit():
        col -= 1
    while info[row][col].isdigit():
        number += info[row][col]
        col += 1
    return int(number)


info = list(sys.stdin)
nonSymbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "\n"]
total = 0

# loops through every character until it finds a symbol
for row in range(len(info)):
    for col in range(len(info[row])):
        # if there's a symbol, add all the numbers around it
        if info[row][col] not in nonSymbols:
            total += sum(checkAround(row, col))

print(total)
