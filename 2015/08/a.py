import sys

count = 0
for line in sys.stdin:
    line = line.strip("\n")
    count += len(line) - len(eval(line))

print(count)
