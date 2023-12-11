# Only thing I can think of is split each block tile into 9
# then work from a dot on the outside
# if it's touching something inside, change it
# when you change it, make sure the barrier is still in place
# after you change to 9 tiles, change everything to inside
# find that dot, and change it to outside
# every time a dot is changed, look at every dot around it
# it's a horrible solution


import sys


def findS(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == "S":
                return [row, col]


def findFirstPos(arr, pos):
    pos = [pos[0], pos[1]]
    if pos[1] != len(arr[pos[0]]) - 1 and arr[pos[0]][pos[1] + 1] in "J7-":
        pos[1] += 1  # right
    elif pos[1] != 0 and arr[pos[0]][pos[1] - 1] in "LF-":
        pos[1] -= 1  # left
    elif pos[0] != len(arr) - 1 and arr[pos[0] + 1][pos[1]] in "JL|":
        pos[0] += 1  # down
    elif pos[0] != 0 and arr[pos[0] - 1][pos[1]] in "7F|":
        pos[0] -= 1  # up
    return [pos[0], pos[1]]


def findNextPos(arr, pos):
    prevPos = [pos[-2][0], pos[-2][1]]
    pos = [pos[-1][0], pos[-1][1]]
    pipe = arr[pos[0]][pos[1]]
    if pipe == "J":
        if pos[0] == prevPos[0]:
            pos[0] -= 1
        else:
            pos[1] -= 1
    elif pipe == "L":
        if pos[0] == prevPos[0]:
            pos[0] -= 1
        else:
            pos[1] += 1
    elif pipe == "F":
        if pos[0] == prevPos[0]:
            pos[0] += 1
        else:
            pos[1] += 1
    elif pipe == "7":
        if pos[0] == prevPos[0]:
            pos[0] += 1
        else:
            pos[1] -= 1
    elif pipe == "|":
        if prevPos[0] < pos[0]:
            pos[0] += 1
        else:
            pos[0] -= 1
    elif pipe == "-":
        if prevPos[1] < pos[1]:
            pos[1] += 1
        else:
            pos[1] -= 1
    return [pos[0], pos[1]]


def convert(arr, pos):
    # simplify everything into tempArr
    tempArr = [["." for i in range(len(arr[x]))] for x in range(len(arr))]
    for p in pos:
        tempArr[p[0]][p[1]] = arr[p[0]][p[1]]

    # make the S into what it actually should be
    if pos[0][1] < pos[1][1]:
        if pos[0][0] < pos[-1][0]:
            s = "F"
        elif pos[0][0] > pos[-1][0]:
            s = "L"
        else:
            s = "-"
    elif pos[0][1] > pos[1][1]:
        if pos[0][0] < pos[-1][0]:
            s = "7"
        elif pos[0][0] > pos[-1][0]:
            s = "J"
        else:
            s = "-"
    else:
        s = "|"
    tempArr[pos[0][0]][pos[0][1]] = s

    # expand everything into newArr
    newArr = [[0 for i in range(3 * len(arr[0]))] for x in range(3 * len(arr))]
    for row in range(len(tempArr)):
        for col in range(len(tempArr[row])):
            pipe = tempArr[row][col]
            if pipe == ".":
                for i in range(3):
                    for x in range(3):
                        newArr[3 * row + i][3 * col + x] = "."
            else:
                for i in range(0, 3, 2):
                    for x in range(0, 3, 2):
                        newArr[3 * row + i][3 * col + x] = "."
                if pipe == "J":
                    up, down, left, right = "#", ".", "#", "."
                elif pipe == "L":
                    up, down, left, right = "#", ".", ".", "#"
                elif pipe == "F":
                    up, down, left, right = ".", "#", ".", "#"
                elif pipe == "7":
                    up, down, left, right = ".", "#", "#", "."
                elif pipe == "|":
                    up, down, left, right = "#", "#", ".", "."
                elif pipe == "-":
                    up, down, left, right = ".", ".", "#", "#"
                newArr[3 * row + 1][3 * col + 1] = "#"
                newArr[3 * row][3 * col + 1] = up
                newArr[3 * row + 2][3 * col + 1] = down
                newArr[3 * row + 1][3 * col] = left
                newArr[3 * row + 1][3 * col + 2] = right

    return newArr


def incrementFlood(arr, pos, unVisited):
    if arr[pos[0]][pos[1]] == ".":
        arr[pos[0]][pos[1]] = "o"
        unVisited.append(pos)


def flood(arr):
    unVisited = [[0, 0]]
    while unVisited:
        if unVisited[0][1] != len(arr[0]) - 1:  # right
            incrementFlood(arr, [unVisited[0][0], unVisited[0][1] + 1], unVisited)
        if unVisited[0][1] != 0:  # left
            incrementFlood(arr, [unVisited[0][0], unVisited[0][1] - 1], unVisited)
        if unVisited[0][0] != len(arr) - 1:  # down
            incrementFlood(arr, [unVisited[0][0] + 1, unVisited[0][1]], unVisited)
        if unVisited[0][0] != 0:  # up
            incrementFlood(arr, [unVisited[0][0] - 1, unVisited[0][1]], unVisited)
        unVisited.pop(0)


def countInside(arr):
    count = 0
    for row in range(1, len(arr), 3):
        for col in range(1, len(arr[row]), 3):
            print(arr[row][col], sep=" ", end="")
            if arr[row][col] == ".":
                count += 1
        print()
    return count


pipes = [i.strip("\n") for i in list(sys.stdin)]

sPos = findS(pipes)
positions = [sPos, findFirstPos(pipes, sPos)]  # stores coordinates of the pipe

# while we haven't gotten back to starting position
while positions[-1][0] != sPos[0] or positions[-1][1] != sPos[1]:
    positions.append(findNextPos(pipes, positions))
positions.pop()

# make it more useable
expandedPipes = convert(pipes, positions)  # make it more useable
for i in expandedPipes:
    print(" ".join(i))
print()

# fill all outside bits with 'o's
flood(expandedPipes)
for i in expandedPipes:
    print(" ".join(i))
print()

print(countInside(expandedPipes))
