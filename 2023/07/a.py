import sys

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def score(hand):
    for card in cards:
        if hand.count(card) == 5:
            return 6
        elif hand.count(card) == 4:
            return 5
        elif hand.count(card) == 3:
            for c in cards:
                if card != c and hand.count(c) == 2:
                    return 4
            return 3
        elif hand.count(card) == 2:
            for c in cards:
                if card != c and hand.count(c) == 3:
                    return 4
            for c in cards:
                if card != c and hand.count(c) == 2:
                    return 2
            return 1
    return 0


def firstLoses(first, second):
    if score(first) < score(second):
        return True
    elif score(first) == score(second):
        for i in range(5):
            if cards.index(first[i]) < cards.index(second[i]):
                return True
            if cards.index(first[i]) > cards.index(second[i]):
                return False
    return False


sets = []
for line in sys.stdin:
    line.strip("\n")
    hand, bid = line.split()
    bid = int(bid)
    sets.append([hand, bid])

for i in range(len(sets)):
    worst = i
    for x in range(i, len(sets)):
        if firstLoses(sets[x][0], sets[worst][0]):
            worst = x
    sets[worst], sets[i] = sets[i], sets[worst]
    print(1000 - i)

answer = 0
for i in range(len(sets)):
    answer += sets[i][1] * (i + 1)

print(answer)
