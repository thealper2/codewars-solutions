def check(m, n):
    if n < m:
        m, n = n, m
    return (m == 3 and (n == 4 or n >= 7)) or (m == 4 and n >= 5) or m > 4
