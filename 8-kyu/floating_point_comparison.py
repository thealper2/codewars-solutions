import math


def approx_equals(a, b):
    return math.isclose(a, b, abs_tol=0.001)
