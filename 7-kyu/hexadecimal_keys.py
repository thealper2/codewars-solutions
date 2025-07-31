import math


def find_key(encryption_key):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    n = int(encryption_key, 16)
    for p in range(2, 10**5):
        if n % p == 0 and is_prime(p):
            q = n // p
            if is_prime(q):
                return (p - 1) * (q - 1)

    return None
