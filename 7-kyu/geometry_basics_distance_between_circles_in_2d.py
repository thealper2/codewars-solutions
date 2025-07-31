import math


def distance_between_circles(a, b):
    dx = a.center.x - b.center.x
    dy = a.center.y - b.center.y
    distance = math.sqrt(dx**2 + dy**2)
    sum_radii = a.radius + b.radius
    if distance <= sum_radii:
        return 0

    return distance - sum_radii
