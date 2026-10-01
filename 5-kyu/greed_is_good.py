from collections import Counter

def score(dice):
    counts = Counter(dice)
    total = 0
    for face in range(1, 7):
        n = counts[face]
        if n >= 3:
            if face == 1:
                total += 1000
            else:
                total += face * 100
            n -= 3
        if face == 1:
            total += n * 100
        elif face == 5:
            total += n * 50

    return total