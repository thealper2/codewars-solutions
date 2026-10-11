import math

def cycle(n) :
    if math.gcd(n, 10) != 1:
        return -1
    
    r = 10 % n
    k = 1
    while r != 1:
        r = r * 10 % n
        k += 1
        
    return k