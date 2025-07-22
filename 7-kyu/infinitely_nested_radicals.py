import math


def fn(x):
    discriminant = 1 + 4 * x
    if discriminant < 0:
        return None
    
    return (1 + math.sqrt(discriminant)) / 2