import sys

numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

total = 0
for line in sys.stdin:
    lindex = 1000
    rindex = -1
    for n in range(len(numbers)):
        ltemp = line.find(numbers[n])
        if ltemp != -1 and lindex > ltemp:
            lindex = ltemp
            left = n % 10
        rtemp = line.rfind(numbers[n])
        if rindex < rtemp:
            rindex = rtemp
            right = n % 10

    num = str(left) + str(right)
    total += int(num)

print(total)
