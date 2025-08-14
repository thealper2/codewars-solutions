def factorial(n):
    if n == 0:
        return 1

    if n < 0 or n > 12:
        raise ValueError()
    
    return n * factorial(n - 1)
