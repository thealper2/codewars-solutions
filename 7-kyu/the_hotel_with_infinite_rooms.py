import math

def group_size(S, D):
    a = 0.5
    b = S - 0.5
    c = -D
    disc = b*b - 4*a*c
    n = math.ceil((-b + math.sqrt(disc)) / (2*a))
    return S + n - 1
