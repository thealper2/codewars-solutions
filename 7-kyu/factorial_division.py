def factorial_division(n, d):
    l = n - d
    fact = 1
    for _ in range(l):
        fact *= n
        n -= 1
        
    return fact
