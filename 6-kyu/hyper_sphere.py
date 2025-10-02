def in_sphere(coords, radius):
    return sum(x**2 for x in coords) <= radius ** 2
