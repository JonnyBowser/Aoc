import sys

cards = list(sys.stdin)
points = [0 for i in range(len(cards))]
total = 0
# go from the end to the beginning to find how much each card is worth
for i in range(len(cards) - 1, -1, -1):
    winning, owned = cards[i].split(":")[1].split("|")
    winning = set([i.strip() for i in winning.split()])
    owned = set([i.strip() for i in owned.split()])
    numWins = len(winning.intersection(owned))
    points[i] = 1
    if numWins > 0:
        points[i] += sum(points[i + 1 : i + 1 + numWins])

for i in points:
    print(i)
print(sum(points))
