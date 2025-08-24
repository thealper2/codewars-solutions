import math


def stereometry(r, h):
    r2 = (r ** 2 - h ** 2) ** 0.5
    r_surface = round(4 * math.pi * (r ** 2), 3)
    r2_area = round(math.pi * (r2 ** 2), 3)
    r2_perimeter = round(2 * math.pi * r2, 3)
    return (r_surface, r2_area, r2_perimeter)
    
