import sys


def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


def lcm(n1, n2):
    n1, n2 = max(n1, n2), min(n1, n2)
    return n1 * n2 / gcd(n1, n2)


def lcmArr(arr):
    arr = list(arr)
    while len(arr) >= 2:
        arr.append(lcm(arr.pop(0), arr.pop(0)))
    return arr[0]


directions = input()
input()

maps = {}
for line in sys.stdin:
    key, _, left, right = line.split()
    left, right = left[1:-1], right[:-1]
    maps[key] = (left, right)

leftRight = {"L": 0, "R": 1}
curr = [i for i in maps if i[-1] == "A"]
factors = []
i = 0
while len(factors) < 6:
    for c in curr:
        if c[-1] == "Z":
            factors.append(i)
    for c in range(len(curr)):
        curr[c] = maps[curr[c]][leftRight[directions[i % len(directions)]]]
    i += 1

print(lcmArr(factors))
