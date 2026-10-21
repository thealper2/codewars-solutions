def last_fib_digit(n):
    period = 60
    idx = ((n - 1) % period) + 1
    a, b = 1, 1
    for _ in range(idx - 1):
        a, b = b, (a + b) % 10
        
    return a