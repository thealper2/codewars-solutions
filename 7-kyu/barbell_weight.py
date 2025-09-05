def barbell_weight(barbell):
    discs = {
        'R': 25,
        'B': 20,
        'Y': 15,
        'G': 10,
        'W': 5,
        'r': 2.5,
        'b': 2,
        'y': 1.5,
        'g': 1,
        'w': 0.5,
        'c': 2.5
    }
    return sum(discs.get(c, 0) for c in barbell) + 20
