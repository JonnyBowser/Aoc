import sys

total = 0
for line in sys.stdin:
    num = ""
    for x in line:
        if x.isdigit():
            num += x
            break
    for x in reversed(line):
        if x.isdigit():
            num += x
            break
    print(num)
    total += int(num)

print(total)
