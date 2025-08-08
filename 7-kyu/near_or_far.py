def common_distance(n, m, A, B):
    ax, ay = A
    bx, by = B
    result = []

    for i in range(n):
        for j in range(m):
            if (i, j) == A or (i, j) == B:
                continue
            d1 = (i - ax) ** 2 + (j - ay) ** 2
            d2 = (i - bx) ** 2 + (j - by) ** 2
            if d1 == d2:
                result.append((i, j))
    
    return sorted(result)
