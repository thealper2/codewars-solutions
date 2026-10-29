def dbl_linear(n):
    u = [1]
    i2 = i3 = 0
    while len(u) <= n:
        next2 = 2 * u[i2] + 1
        next3 = 3 * u[i3] + 1
        nxt = min(next2, next3)
        if nxt == next2:
            i2 += 1
        if nxt == next3:
            i3 += 1
        u.append(nxt)
    return u[n]