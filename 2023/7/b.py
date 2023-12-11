import sys

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def score(hand):
    newHand = str(hand)
    if hand.count("J") > 0:
        if hand.count("J") == 5:
            return 6
        maxCard = "1"
        for card in cards:
            if card != "J" and newHand.count(card) > newHand.count(maxCard):
                maxCard = card
        newHand = newHand.replace("J", maxCard)

    for card in cards:
        if newHand.count(card) == 5:
            return 6
        elif newHand.count(card) == 4:
            return 5
        elif newHand.count(card) == 3:
            for c in cards:
                if card != c and newHand.count(c) == 2:
                    return 4
            return 3
        elif newHand.count(card) == 2:
            for c in cards:
                if card != c and newHand.count(c) == 3:
                    return 4
            for c in cards:
                if card != c and newHand.count(c) == 2:
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

print(sets)
print(answer)
