import sys


def all0(arr):
    for a in arr:
        if a != 0:
            return False
    return True


predictions = []

for line in sys.stdin:
    numbers = [list(map(int, line.split()))]
    while not all0(numbers[-1]):
        numbers.append(
            [numbers[-1][i] - numbers[-1][i - 1] for i in range(1, len(numbers[-1]))]
        )
    predictions.append(sum([num[-1] for num in numbers]))

print(sum(predictions))
