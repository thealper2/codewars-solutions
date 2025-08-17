import math


def cube_volume(h, r):
    base_constraint = r * math.sqrt(2)
    side = min(h, base_constraint)
    volume = side ** 3
    return volume
