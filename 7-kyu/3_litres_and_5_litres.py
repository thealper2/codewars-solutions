import math


def can_measure(a, b, c):
    if c > max(a, b):
        return False
    
    if c % math.gcd(a, b) == 0:
        return True
    
    return False
