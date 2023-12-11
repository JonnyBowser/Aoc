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
total = 0

# loops through every character until it finds a star
for row in range(len(info)):
    for col in range(len(info[row])):
        if info[row][col] == "*":
            # if there's exactly two numbers around it, add their product
            numbers = checkAround(row, col)
            if len(numbers) == 2:
                total += numbers[0] * numbers[1]

print(total)
