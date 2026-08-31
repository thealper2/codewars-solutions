import math

def surjections(n: int, k: int) -> int:
    return sum(((-1) ** i) * math.comb(k, i) * ((k - i) ** n) for i in range(k))