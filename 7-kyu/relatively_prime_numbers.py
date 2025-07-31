import math


def relatively_prime(n, lst):
    return [x for x in lst if math.gcd(n, x) == 1]
