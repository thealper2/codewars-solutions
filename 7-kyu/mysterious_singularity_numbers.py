def real_numbers(n):
    total = n
    total -= n // 2
    total -= n // 3
    total -= n // 5
    total += n // (2*3)
    total += n // (2*5)
    total += n // (3*5)
    total -= n // (2*3*5)
    return total
