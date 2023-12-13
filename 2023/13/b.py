# need to add an enter to the end of input
import sys


def diffArr(arr1, arr2):
    difference = 0
    for row in range(len(arr1)):
        for ch in range(len(arr1[row])):
            if arr1[row][ch] != arr2[row][ch]:
                difference += 1
    return difference


def diffStr(str1, str2):
    difference = 0
    for ch in range(len(str1)):
        if str1[ch] != str2[ch]:
            difference += 1
    return difference


def matches(pattern):
    for rowAbove in range(1, len(pattern)):
        # if there's a vertical line of symmetry
        if (
            diffArr(
                pattern[max(0, rowAbove * 2 - len(pattern)) : rowAbove],
                list(reversed(pattern[rowAbove : min(len(pattern), 2 * rowAbove)])),
            )
            == 1
        ):
            return 100 * rowAbove

    for colLeft in range(1, len(pattern[0])):
        broken = False
        # if there's a horizontal line of symmetry
        difference = 0
        for row in pattern:
            difference += diffStr(
                row[max(0, colLeft * 2 - len(row)) : colLeft],
                "".join(list(reversed(row[colLeft : min(len(row), 2 * colLeft)]))),
            )
        if difference == 1:
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
