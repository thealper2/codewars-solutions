import math


def half_life(initial, remaining, time):
    ratio = remaining / initial
    half_life = -(time * math.log(2)) / math.log(ratio)
    return half_life