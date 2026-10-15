import math

def points(n):
    r2 = n * n
    count = 0
    for x in range(-n, n + 1):
        y2 = r2 - x * x
        y_max = math.isqrt(y2)
        count += 2 * y_max + 1

    return count