import sys

lights = [[0 for i in range(1000)] for x in range(1000)]
for line in sys.stdin:
    line = line.replace(",", " ")
    left, top, right, bottom = [int(i) for i in line.split() if i.isdigit()]
    if "turn on" in line:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                lights[row][col] += 1
    elif "turn off" in line:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                lights[row][col] = max(lights[row][col] - 1, 0)
    else:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                lights[row][col] += 2

count = 0
for row in lights:
    for col in row:
        count += col

print(count)
