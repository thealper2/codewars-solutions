from math import gcd

def nbr_of_laps(x, y):
    l = x * y // gcd(x, y)
    return (l // x, l // y)