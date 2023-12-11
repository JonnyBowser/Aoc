import sys

total = 0
for line in sys.stdin:
    winning, owned = line.split(":")[1].split("|")
    winning = set([i.strip() for i in winning.split()])
    owned = set([i.strip() for i in owned.split()])
    numWins = len(winning.intersection(owned))
    if numWins > 0:
        total += 2 ** (numWins - 1)

print(total)
