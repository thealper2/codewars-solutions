def magical_well(a, b, n):
    total = 0
    for _ in range(n):
        total += a * b
        a += 1
        b += 1

    return total
