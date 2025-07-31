import math


def magnitude(vector):
    sum_of_squares = sum(x**2 for x in vector)
    magnitude = math.sqrt(sum_of_squares)
    return magnitude
