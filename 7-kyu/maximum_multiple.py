def max_multiple(divisor, bound):
    result = 0
    for n in range(0, bound + 1):
        if n % divisor != 0:
            continue

        if n > bound:
            continue

        if n < 0:
            continue

        result = n

    return result
