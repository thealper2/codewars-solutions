import math


def closest_power(x):
    if x < 4:
        return 4
    
    n = int(round(x))
    best = 4
    best_dist = abs(x - 4)
    max_k = int(math.log2(n)) + 2
    
    for k in range(2, max_k + 1):
        m = int(round(n ** (1 / k)))
        for base in (m - 1, m, m + 1):
            if base > 1:
                val = base ** k
                dist = abs(val - x)
                if dist < best_dist or (dist == best_dist and val < best):
                    best = val
                    best_dist = dist
                    
    return best