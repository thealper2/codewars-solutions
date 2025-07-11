import math

def fraction(a, b):
    gcd = math.gcd(a, b)
    return a // gcd + b // gcd
