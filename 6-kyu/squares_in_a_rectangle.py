def find_squares(x,y):
    m = min(x, y)
    n = max(x, y)
    return m * (m + 1) * (3 * n - m + 1) // 6