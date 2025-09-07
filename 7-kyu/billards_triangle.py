def pyramid(balls):
    n = 1
    while n * (n + 1) // 2 <= balls:
        n += 1
        
    return n - 1
