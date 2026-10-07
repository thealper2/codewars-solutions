from collections import Counter


def fruit(reels, spins):
    items = ["Jack", "Queen", "King", "Bar", "Cherry", "Seven", "Shell", "Bell", "Star", "Wild"]
    values = {
        "Wild":   (100, 10, None),
        "Star":   (90, 9, 18),
        "Bell":   (80, 8, 16),
        "Shell":  (70, 7, 14),
        "Seven":  (60, 6, 12),
        "Cherry": (50, 5, 10),
        "Bar":    (40, 4, 8),
        "King":   (30, 3, 6),
        "Queen":  (20, 2, 4),
        "Jack":   (10, 1, 2),
    }

    reels = [reels[i][spins[i]] for i in range(3)]

    counts = Counter(reels)

    if len(counts) == 1:
        item = reels[0]
        return values[item][0]

    if len(counts) == 2:
        for item, cnt in counts.items():
            if cnt == 2:
                pair_item = item
                break
        other = [x for x in reels if x != pair_item][0]
        if other == "Wild":
            v = values[pair_item][2]
            return v if v is not None else 0
        else:
            return values[pair_item][1]

    return 0