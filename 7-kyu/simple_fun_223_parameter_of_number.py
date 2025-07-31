import math


def parameter(n):
    product = 1
    sum_digits = 0
    i = 0

    while 10**i <= n:
        d = n // 10**i % 10
        product *= d
        sum_digits += d
        i += 1

    return math.lcm(product, sum_digits)
