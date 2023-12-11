import sys

# make values in the form of [[[start1, end1], [start2, end2]]]
seeds = [int(i) for i in input().split()[1::]]
values = [[]]
for i in range(0, len(seeds), 2):
    start = seeds[i]
    end = start + seeds[i + 1] - 1
    values[0].append([start, end])


# make categories in the form of [[[dest, start, range], [dest, start, range]]]
categories = []
inputNumbers = False
for line in sys.stdin:
    if line == "\n":
        inputNumbers = False
    elif not line[0].isdigit():
        categories.append([])
        inputNumbers = True
    elif inputNumbers:
        categories[-1].append(list(map(int, line.split())))


# go through every map
for i in range(len(categories)):
    categories[i].sort(key=lambda x: x[1])  # sort by starting value
    values.append([])
    # go through every value range
    for valueRange in values[i]:
        start, end = valueRange
        # first split up the valueRange using the start
        # and convert those to where they should go
        broke = False
        for map in categories[i]:
            low = map[1]
            high = low + map[2] - 1
            diff = low - map[0]
            if end <= high:
                if start < low <= end:
                    values[i + 1].append([start, low - 1])
                    values[i + 1].append([low - diff, end - diff])
                elif end < low:
                    values[i + 1].append([start, end])
                else:
                    values[i + 1].append([start - diff, end - diff])
                broke = True
                break
            else:
                if start < low:
                    values[i + 1].append([start, low - 1])
                    values[i + 1].append([low - diff, high - diff])
                    start = high + 1
                elif start <= high:
                    values[i + 1].append([start - diff, high - diff])
                    start = high + 1
        if not broke:
            values[i + 1].append([start, end])

# find the minimum after converting everything to location
print(min([i[0] for i in values[-1]]))
