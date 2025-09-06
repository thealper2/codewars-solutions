import math


def coordinates(degrees, radius):
    rad = math.radians(degrees)
    x = radius * math.cos(rad)
    y = radius * math.sin(rad)
    return (round(x, 10), round(y, 10))
