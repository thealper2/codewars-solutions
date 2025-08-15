import math


def find_next_power(val, pow_):
    p = 1
    a = 1
    while p <= val:
        p = math.pow(a, pow_)
        a += 1
        
    return p
