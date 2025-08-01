def step(x, y):
    if x == y:
        return 0
    D = y - x
    k = int(D**0.5)
    if k * k == D:
        return 2 * k - 1
    elif D <= k * (k + 1):
        return 2 * k
    else:
        return 2 * k + 1
