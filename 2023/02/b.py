import sys

total = 0
for line in sys.stdin:
    sets = (line.split(":")[1]).split(";")
    red, green, blue = 0, 0, 0

    # go through every set
    for s in sets:
        colors = s.split(",")

        # go through every color in the set
        for color in colors:
            count, color = color.split()
            count, color = int(count), color.strip()

            # update the max color values
            if color == "red":
                red = max(count, red)
            elif color == "green":
                green = max(count, green)
            elif color == "blue":
                blue = max(count, blue)

    total += red * green * blue

print(total)
