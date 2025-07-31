import math


def sum_circles(*args):
    total_area = 0
    for d in args:
        radius = d / 2
        area = math.pi * (radius**2)
        total_area += area

    return f"We have this much circle: {round(total_area)}"
