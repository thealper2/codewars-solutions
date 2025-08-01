import math


def solve(s,g):
    for i in range(s + 1):
        j = s - i
        if math.gcd(i, j) == g:
            return (i, j)
    
    return -1
