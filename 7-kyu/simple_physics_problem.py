def solveit(vi, vf, t):
    if vi > vf:
        return []
    a = (vf - vi) / t
    d = vi * t + 0.5 * a * t**2
    return [round(a, 2), round(d, 2)]
