import math


def triangle_perimeter(triangle):
    ab = math.sqrt((triangle.b.x - triangle.a.x) ** 2 + (triangle.b.y - triangle.a.y) ** 2)
    bc = math.sqrt((triangle.c.x - triangle.b.x) ** 2 + (triangle.c.y - triangle.b.y) ** 2)
    ca = math.sqrt((triangle.a.x - triangle.c.x) ** 2 + (triangle.a.y - triangle.c.y) ** 2)
    return ab + bc + ca
