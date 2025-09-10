def n_bonacci_ratio(n):
    if n == 0:
        return 0.0
    
    a, b = 0.0, 1.0
    for _ in range(100):
        a, b = b, n * b + a
        
    return b / a
