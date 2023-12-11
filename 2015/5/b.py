def rule1(s):
    for i in range(len(s) - 1):
        if s[i : i + 2] in s[:i] or s[i : i + 2] in s[i + 2 :]:
            return True
    return False


def rule2(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


def rules(s):
    if rule1(s) and rule2(s):
        return True
    return False


import sys

count = 0
for line in sys.stdin:
    if rules(line):
        count += 1

print(count)
