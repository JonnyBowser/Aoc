time = int("".join(input().split()[1:]))
distance = int("".join(input().split()[1:]))

print(len([x for x in range(time) if distance < x * (time - x)]))
