def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID"

    return sum([_ for _ in range(n, m, n)])
