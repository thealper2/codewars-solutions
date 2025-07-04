import math

def all_nines(x):
    if x == 1:
        return 9

    if math.gcd(x, 10) != 1:
        return -1
    
    k = 1
    remainder = 10 % x
    while remainder != 1:
        remainder = (remainder * 10) % x
        k += 1
        if k > x:
            return -1

    m = (10**k - 1) // x
    return m
