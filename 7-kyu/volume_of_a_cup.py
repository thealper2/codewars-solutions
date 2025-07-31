import math


def cup_volume(d1, d2, height):
    r_1 = d1 / 2
    r_2 = d2 / 2
    volume = (1 / 3) * math.pi * height * (r_1**2 + r_1 * r_2 + r_2**2)
    return volume
