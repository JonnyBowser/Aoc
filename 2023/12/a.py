import sys
from typing import List


def countSolutions(sectionOfSprings: str, reqs: List[int]) -> int:
    if not reqs:
        if "#" not in sectionOfSprings:
            return 1
        else:
            return 0
    elif sum(reqs) + len(reqs) - 1 > len(sectionOfSprings):
        return 0

    numSolutions = 0
    if "." not in sectionOfSprings[: reqs[0]] and (
        reqs[0] >= len(sectionOfSprings) or sectionOfSprings[reqs[0]] != "#"
    ):
        numSolutions += countSolutions(sectionOfSprings[reqs[0] + 1 :], reqs[1::])
    if sectionOfSprings[0] != "#":
        numSolutions += countSolutions(sectionOfSprings[1:], reqs)
    return numSolutions


springs, reqs = [], []
for line in sys.stdin:
    currSprings, currReqs = line.split()
    springs.append(currSprings)
    reqs.append(list(map(int, currReqs.split(","))))

totalOptions = 0
for rowIndex in range(len(springs)):
    totalOptions += countSolutions(springs[rowIndex], reqs[rowIndex])

print(totalOptions)
