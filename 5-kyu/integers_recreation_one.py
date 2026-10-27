import math


def list_squared(m, n):
    result = []
    for x in range(m, n + 1):
        total = 0
        r = math.isqrt(x)
        for d in range(1, r + 1):
            if x % d == 0:
                total += d * d
                e = x // d
                if e != d:
                    total += e * e
        s = math.isqrt(total)
        if s * s == total:
            result.append([x, total])
    return result