import sys

count = 0
for line in sys.stdin:
    quote = line.count('"')
    back = line.count("\\")
    count += 2 + back + quote

print(count)
