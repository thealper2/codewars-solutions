import math


def perfect_roots(n):
    sqrt_2nd = math.isqrt(n)
    if sqrt_2nd * sqrt_2nd != n:
        return False

    sqrt_4th = math.isqrt(sqrt_2nd)
    if sqrt_4th * sqrt_4th != sqrt_2nd:
        return False

    sqrt_8th = math.isqrt(sqrt_4th)
    if sqrt_8th * sqrt_8th != sqrt_4th:
        return False

    return True
