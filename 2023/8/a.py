import sys

directions = input()
input()

maps = {}
for line in sys.stdin:
    key, _, left, right = line.split()
    left, right = left[1:-1], right[:-1]
    maps[key] = (left, right)

leftRight = {"L": 0, "R": 1}
curr = "AAA"
i = 0
while curr != "ZZZ":
    curr = maps[curr][leftRight[directions[i % len(directions)]]]
    i += 1

print(i)
