def dist(v, mu):
    v_ms = v * 1000 / 3600
    g = 9.81
    t = 1.0
    return v_ms * t + v_ms * v_ms / (2 * mu * g)

def speed(d, mu):
    g = 9.81
    t = 1.0
    a = 1.0 / (2 * mu * g)
    b = t
    c = -d
    disc = b * b - 4 * a * c
    v_ms = (-b + disc**0.5) / (2 * a)
    return v_ms * 3600 / 1000