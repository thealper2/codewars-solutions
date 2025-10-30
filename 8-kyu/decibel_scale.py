import math


def db_scale(intensity):
    return 10 * math.log10(intensity) + 120
