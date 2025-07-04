import math


def binary_gcd(x, y):
    if x == 0 and y == 0:
        return 0
    
    x = abs(x)
    y = abs(y)
    
    g = math.gcd(x, y)
    binary = bin(g)
    return binary.count('1')
