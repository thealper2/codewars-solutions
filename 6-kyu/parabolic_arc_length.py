import math

def len_curve(n):
    h = 1.0 / n
    total_length = 0.0

    for i in range(n):
        x0 = i * h
        y0 = x0 * x0
        x1 = (i + 1) * h
        y1 = x1 * x1

        segment_length = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        total_length +=  segment_length

    return total_length