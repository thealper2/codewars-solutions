def pyramid(s):
    # v = n + 1
    # e = 2n
    # f = n + 1
    # 4n + 2 = 42 = s
    n = (s - 2) / 4
    return (n + 1, 2 * n, n + 1, n)
