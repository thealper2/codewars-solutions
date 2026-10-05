import math

def tankvol(h, d, vt):
    r = d / 2

    angle = 2 * math.acos((r - h) / r)

    segment_area = (
        r ** 2 / 2 * (angle - math.sin(angle))
    )

    circle_area = math.pi * r ** 2

    return int(vt * segment_area / circle_area)