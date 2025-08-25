import math


def bounce_count(h, w, v):
    g = 9.81
    t = math.sqrt(2 * h / g)
    distance = v * t
    bounces = distance // w
    return bounces
