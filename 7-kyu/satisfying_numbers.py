import math


def smallest(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = math.lcm(lcm, i)
        
    return lcm
