def perimeter(n):
    a, b = 1, 1
    total = 0
    for _ in range(n + 1):
        total += a
        a, b = b, a + b

    return 4 * total