import sys


def all0(arr):
    for a in arr:
        if a != 0:
            return False
    return True


def findValue(arr):
    value = sum(
        [arr[-2 - i][0] if i % 2 == 0 else -arr[-2 - i][0] for i in range(len(arr) - 1)]
    )
    return value if len(arr) % 2 == 0 else -value


predictions = []

for line in sys.stdin:
    numbers = [list(map(int, line.split()))]
    while not all0(numbers[-1]):
        numbers.append(
            [numbers[-1][i] - numbers[-1][i - 1] for i in range(1, len(numbers[-1]))]
        )
    predictions.append(findValue(numbers))

print(sum(predictions))
