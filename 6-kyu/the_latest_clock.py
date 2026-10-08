from itertools import permutations

def latest_clock(a, b, c, d):
    best = None
    for h1, h2, m1, m2 in set(permutations([a, b, c, d])):
        hour = h1 * 10 + h2
        minute = m1 * 10 + m2
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            t = hour * 60 + minute
            if best is None or t > best:
                best = t

    h, m = divmod(best, 60)
    return f'{h:02d}:{m:02d}'