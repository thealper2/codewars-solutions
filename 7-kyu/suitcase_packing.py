def fit_in(a, b, m, n):
    max_square = max(a, b)
    if max_square > m or max_square > n:
        return False
    
    if (a + b) <= m and max(a, b) <= n:
        return True
    
    if (a + b) <= n and max(a, b) <= m:
        return True
    
    return False
