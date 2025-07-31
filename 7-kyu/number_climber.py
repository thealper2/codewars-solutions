def climb(n):
    sequence = []
    while n >= 1:
        sequence.insert(0, n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n - 1) // 2

    return sequence
