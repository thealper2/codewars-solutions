def poly_subtract(p1, p2):
    n, m = len(p1), len(p2)
    if n < m:
        for _ in range(m - n):
            p1.append(0)
            
    elif m < n:
        for _ in range(n - m):
            p2.append(0)
            
    return [a - b for a, b in zip(p1, p2)]
