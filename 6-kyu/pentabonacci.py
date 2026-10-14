def count_odd_penta_fib(n):
    if n <= 0:
        return 0
    
    if n <= 4:
        return 1
    
    return (n // 6) * 2 - 1 + min(2, n % 6)