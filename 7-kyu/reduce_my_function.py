import math


def reduce_fraction(fraction):
    numerator, denominator = fraction
    gcd_value = math.gcd(numerator, denominator)
    reduced_num = numerator // gcd_value
    reduced_den = denominator // gcd_value
    return (reduced_num, reduced_den)
