import math


def nearest_sq(n):
    sqrt_n = int(math.sqrt(n))

    lower_sq = sqrt_n**2
    higher_sq = (sqrt_n + 1) ** 2

    if abs(n - lower_sq) < abs(n - higher_sq):
        return lower_sq
    else:
        return higher_sq
