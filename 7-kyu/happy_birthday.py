def wrap(h, w, l):
    sides = [h, w, l]
    sides.sort()
    return (sides[0] * 4 + (sides[1] + sides[2]) * 2) + 20
