def digits(n):
    if n < 0:
        n *= -1

    if n == 0:
        return 1

    count = 0
    while n > 0:
        n //= 10
        count += 1

    return count
