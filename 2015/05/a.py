def rule1(s):
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
            if count >= 3:
                return True
    return False


def rule2(s):
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) * 2 in s:
            return True
    return False


def rule3(s):
    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in s:
            return False
    return True


def rules(s):
    if rule1(s) and rule2(s) and rule3(s):
        return True
    return False


import sys

count = 0
for line in sys.stdin:
    if rules(line):
        count += 1

print(count)
