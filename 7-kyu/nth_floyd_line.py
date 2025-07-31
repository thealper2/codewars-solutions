def nth_floyd(n):
    i = 1
    while True:
        lb = (i * (i - 1)) // 2 + 1
        ub = (i * (i + 1)) // 2
        if lb <= n <= ub:
            return i

        i += 1
