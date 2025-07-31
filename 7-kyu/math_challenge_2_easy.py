import math


def radii(a, b, c):
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    r = A / s
    R = (a * b * c) / (4 * A)
    return (r, R)
