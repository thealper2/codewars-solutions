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

def backwards_prime(start, stop):
    result = []
    for n in range(start, stop + 1):
        if is_prime(n):
            r = int(str(n)[::-1])
            if r != n and is_prime(r):
                result.append(n)

    return result