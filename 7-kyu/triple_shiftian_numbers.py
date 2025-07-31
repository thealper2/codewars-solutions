def triple_shiftian(base, n):
    t = base
    for i in range(3, n + 1):
        d = 4 * t[i - 1] - 5 * t[i - 2] + 3 * t[i - 3]
        t.append(d)

    return t[n]
