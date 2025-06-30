import math


def find_slope(points):
    a, b, c, d = points
    if c - a == 0:
        return "undefined"

    slope = math.floor((d - b) / (c - a))
    return str(f"{slope:.0f}")
