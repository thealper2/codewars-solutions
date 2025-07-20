import math


def does_fred_need_houseboat(x,y):
    distance_squared = x**2 + y**2
    N = (math.pi * distance_squared) / 100
    return math.ceil(N)