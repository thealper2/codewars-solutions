def epidemic(tm, n, s0, i0, b, a):
    dt = tm / n
    s, i, r = s0, i0, 0
    max_i = i
    for _ in range(n):
        ds = -dt * b * s * i
        di = dt * (b * s * i - a * i)
        dr = dt * a * i
        s += ds
        i += di
        r += dr
        if i > max_i:
            max_i = i
            
    return int(max_i)