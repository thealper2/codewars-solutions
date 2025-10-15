def zeros(n: int) -> int:
    if n == 0:
        return 0
    
    if n == 1:
        return 2
    
    a, b = 1, 0
    for i in range(2, n + 1):
        a, b = a + b, a
        
    return a + b
