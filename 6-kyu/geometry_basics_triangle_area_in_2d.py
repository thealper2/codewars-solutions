from preloaded import Point, Triangle


def triangle_area(triangle: Triangle) -> float:
    a = triangle.a
    b = triangle.b
    c = triangle.c
    
    area = abs(
        a.x * (b.y - c.y) +
        b.x * (c.y - a.y) +
        c.x * (a.y - b.y)
    ) / 2.0
    
    return round(area, 6)
