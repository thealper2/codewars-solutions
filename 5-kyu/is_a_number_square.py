from math import isqrt

_SQ256 = frozenset((i * i) & 255 for i in range(256))

def is_square(n):
    if n < 0:
        return False

    if n & 255 not in _SQ256:
        return False

    r = isqrt(n)
    return r * r == n