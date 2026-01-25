def polygon_area(a, b, c, d):
    square = b * c
    tri = (c - a) * d
    return square - tri
