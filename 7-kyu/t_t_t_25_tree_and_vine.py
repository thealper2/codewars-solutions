import math


def vine_length(n, height, radius):
    circumference = 2 * math.pi * radius
    base = circumference * n
    length = math.sqrt(base**2 + height**2)
    return length
