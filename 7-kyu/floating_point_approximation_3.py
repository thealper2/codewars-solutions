import math


def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    sqrt_discriminant = math.sqrt(discriminant)

    if b > 0:
        x2 = (2 * c) / (-b - sqrt_discriminant)
    else:
        x2 = (2 * c) / (-b + sqrt_discriminant)

    return x2
