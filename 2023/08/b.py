import sys


def allZ(curr):
    for c in curr:
        if c[-1] != "Z":
            return False
    return True


directions = input()
input()

maps = {}
for line in sys.stdin:
    key, _, left, right = line.split()
    left, right = left[1:-1], right[:-1]
    maps[key] = (left, right)

leftRight = {"L": 0, "R": 1}
curr = [i for i in maps if i[-1] == "A"]
i = 0
while not allZ(curr):
    for c in range(len(curr)):
        curr[c] = maps[curr[c]][leftRight[directions[i % len(directions)]]]
    i += 1

print(i)
