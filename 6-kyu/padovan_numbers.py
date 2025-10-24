def padovan(n):
    if n <= 2:
        return 1
    
    a, b, c = 1, 1, 1
    for i in range(3, n + 1):
        next_val = a + b
        a, b, c = b, c, next_val
    
    return c
