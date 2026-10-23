def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

def is_twinprime(n):
    return is_prime(n) and (is_prime(n - 2) or is_prime(n + 2))