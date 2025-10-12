import math

def next_smaller_pronic(n):
    if n < 2:
        return 0
    
    max_i = int(math.isqrt(n)) + 1
    for i in range(max_i, 0, -1):
        pronic = i * (i + 1)
        if pronic < n:
            return pronic
        
    return 0
