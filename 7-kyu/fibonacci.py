def fibonacci(n: int) -> int:
    fib = [0, 1]
    for i in range(1, n):
        fib.append(fib[i] + fib[i - 1])
    return fib[n]
