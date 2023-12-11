import sys


def findS(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == "S":
                return [row, col]


def findFirstPos(arr, pos):
    pos = [pos[0], pos[1]]
    if pos[1] != len(arr[pos[0]]) - 1 and arr[pos[0]][pos[1] + 1] in "J7-":
        pos[1] += 1
    elif pos[1] != 0 and arr[pos[0]][pos[1] - 1] in "LF-":
        pos[1] -= 1
    elif pos[0] != len(arr) - 1 and arr[pos[0] + 1][pos[1]] in "JL|":
        pos[0] += 1
    elif pos[0] != 0 and arr[pos[0] - 1][pos[1]] in "7F|":
        pos[0] -= 1
    return [pos[0], pos[1]]


def updatePos(arr, prevPos, pos):
    pos = [pos[0], pos[1]]
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


pipes = list(sys.stdin)

sPos = findS(pipes)
prevPos = sPos
currPos = findFirstPos(pipes, sPos)
count = 1
while currPos[0] != sPos[0] or currPos[1] != sPos[1]:
    prevPos, currPos = currPos, updatePos(pipes, prevPos, currPos)
    count += 1

print(count / 2)
