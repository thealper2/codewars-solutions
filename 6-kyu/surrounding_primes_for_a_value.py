def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def prime_bef_aft(num):
    befPrime = num - 1
    aftPrime = num + 1

    while not is_prime(befPrime):
        befPrime -= 1

    while not is_prime(aftPrime):
        aftPrime += 1

    return [befPrime, aftPrime]