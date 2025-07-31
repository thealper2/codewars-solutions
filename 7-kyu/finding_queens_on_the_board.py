def queens(n):
    if n <= 2:
        return 0

    return (n - 1) * (n - 2)
