def even_fib(n):
    a, b = 0, 1
    total = 0
    while b < n:
        if b % 2 == 0:
            total += b
        
        a, b = b, a + b
            
    return total