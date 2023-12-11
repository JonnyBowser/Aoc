import sys

total = 0
for line in sys.stdin:
    good = True
    id, sets = line.split(":")
    id, sets = int(id.split()[1]), sets.split(";")

    # go through every set
    for s in sets:
        colors = s.split(",")

        # go through every color in the set
        for color in colors:
            count, color = color.split()
            count, color = int(count), color.strip("\n ")

            # make sure the number of dice follows the rules
            if not good:
                break
            if color == "red":
                good = count <= 12
            elif color == "green":
                good = count <= 13
            elif color == "blue":
                good = count <= 14

    if good:
        total += id


print(total)
