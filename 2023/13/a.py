# need to add an enter to the end of input
import sys


def matches(pattern):
    for rowAbove in range(1, len(pattern)):
        # if there's a vertical line of symmetry
        if pattern[max(0, rowAbove * 2 - len(pattern)) : rowAbove] == list(
            reversed(pattern[rowAbove : min(len(pattern), 2 * rowAbove)])
        ):
            return 100 * rowAbove

    for colLeft in range(1, len(pattern[0])):
        broken = False
        # if there's a horizontal line of symmetry
        for row in pattern:
            if row[max(0, colLeft * 2 - len(row)) : colLeft] != "".join(
                list(reversed(row[colLeft : min(len(row), 2 * colLeft)]))
            ):
                broken = True
                break
        if not broken:
            return colLeft


pattern = []

total = 0
for line in sys.stdin:
    line = line.strip("\n")
    if line:
        pattern.append(line)
    else:
        total += matches(pattern)
        pattern = []

total += matches(pattern)
print(total)
