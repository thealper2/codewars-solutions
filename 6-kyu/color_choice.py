import math

def checkchoose(m, n):
    for x in range(n + 1):
        if math.comb(n, x) == m:
            return x

    return -1