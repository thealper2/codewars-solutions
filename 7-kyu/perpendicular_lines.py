def perpendicular(n):
    if n < 2:
        return 0
    
    h = n // 2
    v = n - h
    return h * v
