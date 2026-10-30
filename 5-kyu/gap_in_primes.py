def is_prime(n):
    if n < 2:
        return False

    if n < 4:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True

def gap(g, m, n):
    prev = None
    for x in range(m, n + 1):
        if is_prime(x):
            if prev is not None and x - prev == g:
                return [prev, prev + g]

            prev = x

    return None