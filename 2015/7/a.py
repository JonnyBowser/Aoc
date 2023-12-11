import sys


def complement(n):
    s = bin(n)[2:]
    s = "0" * (16 - len(s)) + s
    result = ""
    for ch in s:
        if ch == "1":
            result += "0"
        else:
            result += "1"
    return int(result, 2)


info = list(sys.stdin)
wires = dict()

while len(info) > 0:
    removeThese = []

    for i in range(len(info)):
        line = info[i]
        line = line.strip("\n").split()
        if line[0] == "NOT":
            if line[1] in wires:
                wires[line[3]] = complement(wires[line[1]])
                removeThese.insert(0, i)
        elif line[1] == "->":
            if line[0].isdigit():
                wires[line[2]] = int(line[0])
                removeThese.insert(0, i)
            elif line[0] in wires:
                wires[line[2]] = wires[line[0]]
                removeThese.insert(0, i)
        elif line[1] == "AND":
            if line[0].isdigit() and line[2] in wires:
                wires[line[4]] = int(line[0]) & wires[line[2]]
                removeThese.insert(0, i)
            elif line[0] in wires and line[2] in wires:
                wires[line[4]] = wires[line[0]] & wires[line[2]]
                removeThese.insert(0, i)
        elif line[1] == "OR":
            if line[0] in wires and line[2] in wires:
                wires[line[4]] = wires[line[0]] | wires[line[2]]
                removeThese.insert(0, i)
        elif line[1] == "LSHIFT":
            if line[0] in wires:
                wires[line[4]] = wires[line[0]] << int(line[2])
                removeThese.insert(0, i)
        elif line[1] == "RSHIFT":
            if line[0] in wires:
                wires[line[4]] = wires[line[0]] >> int(line[2])
                removeThese.insert(0, i)

    for i in removeThese:
        info.pop(i)

print(wires["a"])
