def is_triangular(t):
    triangular = 0
    n = 1
    while triangular <= t:
        triangular = n * (n + 1) // 2 
        n += 1
        if triangular == t:
            return True
        
        
    return False
