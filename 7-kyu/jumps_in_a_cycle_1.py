import math


def get_jumps(cycle_list, k):
    n = len(cycle_list)
    g = math.gcd(n, k)
    return n // g
