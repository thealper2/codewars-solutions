import math


def blood_moon(r):
    if r == 0:
        return 0

    acd = math.pi * math.pow(r, 2) / 4
    fe = math.sqrt(2 * (r**2)) / 2
    afe = math.pi * math.pow(fe, 2) / 4
    afe_triangle = (fe * fe) / 2
    fa_r = (math.sqrt(2 * (fe**2))) / 2
    eha = afe - afe_triangle
    agf = math.pi * math.pow(fa_r, 2) / 2
    return agf - eha
