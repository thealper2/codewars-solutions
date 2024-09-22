import math

def square_area(A):
    # 2 * pi * r = 4 * A
    r = (4 * A) / (2 * math.pi)
    return round(r ** 2, 2)