import math

times = list(map(int, input().split()[1:]))
distances = list(map(int, input().split()[1:]))

print(
    math.prod(
        [
            len([x for x in range(times[i]) if distances[i] < x * (times[i] - x)])
            for i in range(len(times))
        ]
    )
)
