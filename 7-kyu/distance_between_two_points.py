import math


def distance(p1, p2):
    if len(p1) != len(p2):
        return -1
    
    if len(p1) == 0:
        return -1
    
    sum_squared = 0.0
    for a, b in zip(p1, p2):
        sum_squared += (a - b) ** 2
    
    return math.sqrt(sum_squared)
