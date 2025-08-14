def is_fibo(a: int, b: int, f: int) -> bool:
    if f == a or f == b:
        return True
    
    fib = [a, b]
    while fib[-1] < f:
        fib.append(fib[-1] + fib[-2])
    
    return fib[-1] == f
