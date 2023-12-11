import sys

lights = [[False for i in range(1000)] for x in range(1000)]
for line in sys.stdin:
    line = line.replace(",", " ")
    left, top, right, bottom = [int(i) for i in line.split() if i.isdigit()]
    if "turn on" in line:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                lights[row][col] = True
    elif "turn off" in line:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                lights[row][col] = False
    else:
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                lights[row][col] = not lights[row][col]

count = 0
for row in lights:
    for col in row:
        if col:
            count += 1

print(count)
