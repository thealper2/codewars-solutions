import math


def crusoe(n, d, ang, dist_mult, ang_mult):
    x, y = 0, 0
    ang0 = math.radians(ang)
    d0 = d
    for _ in range(n):
        x += d0 * math.cos(ang0)
        y += d0 * math.sin(ang0)
        d0 *= dist_mult
        ang0 *= ang_mult
        
    return (x, y)
