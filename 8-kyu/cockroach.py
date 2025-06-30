import math


def cockroach_speed(s):
    cm = 1000 * s * 100
    return math.floor(cm / 3600)
