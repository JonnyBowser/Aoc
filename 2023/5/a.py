import sys

values = [[int(i) for i in input().split()[1::]]]
# values will be where all values after conversion is stored
# values[0] is the values before any conversions
# values[1] is the values after one conversion
# and so on

categories = []  # the conversion data
inputNumbers = False
for line in sys.stdin:
    if line == "\n":
        inputNumbers = False
    elif not line[0].isdigit():
        categories.append([])
        inputNumbers = True
    elif inputNumbers:
        categories[-1].append(list(map(int, line.split())))


# go through each map (ex. seed-to-soil map)
for i in range(len(categories)):
    values.append([])
    # go through every value
    for value in values[i]:
        converted = False
        # convert the value based on the map
        for map in categories[i]:
            converted = False
            end, start, range = map
            if start <= value < start + range:
                values[i + 1].append(value - (start - end))
                converted = True
                break
        if not converted:
            values[i + 1].append(value)

# find the minimum after converting everything to location
print(min(values[-1]))
