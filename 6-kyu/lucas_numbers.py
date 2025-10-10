def lucasnum(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    
    if n > 1:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    else:
        a, b = 2, 1
        for _ in range(-1, n - 1, -1):
            a, b = b - a, a
            
        return a
