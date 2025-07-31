import math


def roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None

    sum_roots = -b / a
    return round(sum_roots, 2)
