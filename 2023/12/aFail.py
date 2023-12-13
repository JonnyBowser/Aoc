import sys, math


# true if everything works
def works(posInRow, rowIndex, reqIndex):
    if not worksCenter(posInRow, rowIndex, reqIndex):
        return False
    if not worksLeft(posInRow, rowIndex, reqIndex):
        return False
    if not worksRight(posInRow, rowIndex, reqIndex):
        return False
    return True


# true if the requirement works at that position
def worksCenter(posInRow, rowIndex, reqIndex):
    leftPos, rightPos = posInRow, posInRow + reqs[rowIndex][reqIndex]
    row = springs[rowIndex][leftPos:rightPos]
    for r in row:
        if r == ".":
            return False
    if (leftPos != 0 and springs[rowIndex][leftPos - 1] == "#") or (
        rightPos != len(springs[rowIndex]) and springs[rowIndex][rightPos] == "#"
    ):
        return False
    return True


# pretty much the exact same as worksCenter, but I'm lazy
def fits(row, posInRow, req):
    leftPos, rightPos = posInRow, posInRow + req
    sectionInRow = row[leftPos:rightPos]
    for r in sectionInRow:
        if r == ".":
            return False
    if (leftPos != 0 and row[leftPos - 1] == "#") or (
        rightPos != len(row) and row[rightPos] == "#"
    ):
        return False
    return True


# true if the requirements to the left could work
def worksLeft(posInRow, rowIndex, reqIndex):
    leftRow = [] if posInRow == 0 else springs[rowIndex][: posInRow - 1]
    leftReqs = reqs[rowIndex][:reqIndex:]
    leftPos = 0
    numFits = 0
    for req in leftReqs:
        while leftPos + req <= len(leftRow):
            if fits(leftRow, leftPos, req):
                numFits += 1
                leftPos += req + 1
                break
            leftPos += 1
    return numFits == len(leftReqs)


# true if the requirements to the right could work
def worksRight(posInRow, rowIndex, reqIndex):
    rightRow = springs[rowIndex][posInRow + reqs[rowIndex][reqIndex] + 1 :]
    rightReqs = reqs[rowIndex][reqIndex + 1 : :]
    rightPos = len(rightRow) - 1
    numFits = 0
    for req in reversed(rightReqs):
        rightPos -= req - 1
        while rightPos >= 0:
            if fits(rightRow, rightPos, req):
                numFits += 1
                rightPos -= 2
                break
            rightPos -= 1
    return numFits == len(rightReqs)


# create and fill springs, and reqs
springs, reqs = [], []
for line in sys.stdin:
    currSprings, currReq = line.split()
    springs += [currSprings]
    reqs += [list(map(int, currReq.split(",")))]

totalOptions = 0
# for each number find how many spots it could go
for rowIndex in range(len(springs)):
    optionsForEachReq = [0 for i in range(len(reqs[rowIndex]))]
    # for each requirement at a certain row
    for reqIndex in range(len(reqs[rowIndex])):
        # check all the positions in the row
        for posInRow in range(len(springs[rowIndex]) - reqs[rowIndex][reqIndex] + 1):
            if works(posInRow, rowIndex, reqIndex):
                optionsForEachReq[reqIndex] += 1
    print(optionsForEachReq)
    totalOptions = math.prod(optionsForEachReq)
print(totalOptions)

# now, I need to use recursion.
