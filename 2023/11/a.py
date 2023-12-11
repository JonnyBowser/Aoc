import sys

sky = list(sys.stdin)
rows = [1 for i in range(len(sky))]  # will keep track if if a certain row has galaxies
cols = [1 for i in range(len(sky[0]))]  # 1 means no galaxies in that row/col
galaxies = []

for row in range(len(sky)):
    for col in range(len(sky[row])):
        if sky[row][col] == "#":
            galaxies.append([row, col])
            rows[row] = 0
            cols[col] = 0

numGalaxies = len(galaxies)
totalDistance = 0
# find the positive x value
minusValue = 0
galaxies.sort(key=lambda x: x[1], reverse=True)
for galaxy in galaxies:
    xDistanceFrom0 = galaxy[1] + sum(cols[: galaxy[1]])
    totalDistance += xDistanceFrom0 * (numGalaxies - 1 - minusValue)
    minusValue += 2

# add that to the positive y value
minusValue = 0
galaxies.sort(key=lambda x: x[0], reverse=True)
for galaxy in galaxies:
    yDistanceFrom0 = galaxy[0] + sum(rows[: galaxy[0]])
    totalDistance += yDistanceFrom0 * (numGalaxies - 1 - minusValue)
    minusValue += 2

print(totalDistance)
