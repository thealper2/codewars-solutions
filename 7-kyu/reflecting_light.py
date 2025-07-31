import math


def reflections(max_x, max_y):
    gcd = math.gcd(max_x, max_y)
    lcm = (max_x * max_y) // gcd
    x_reflections = lcm // max_x
    y_reflections = lcm // max_y
    return (x_reflections % 2 == 1) and (y_reflections % 2 == 1)
