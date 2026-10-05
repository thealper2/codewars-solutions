def fortune(f0, p, c0, n, i):
    f = f0
    c = c0
    
    for _ in range(1, n):
        f = int(f + f * p / 100 - c)
        c = int(c + c * i / 100)
        
        if f < 0:
            return False
        
    return True