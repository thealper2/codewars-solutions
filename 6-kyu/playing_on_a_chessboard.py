import math

def game(n):
    num = n * n
    den = 2
    g = math.gcd(num, den)
    num //= g
    den //= g
    if den == 1:
        return [num]
    
    return [num, den]