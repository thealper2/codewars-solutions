def channelling_primes(n):
    result = 2
    primes = [2]

    for i in range(3, n + 1, 2):
        is_prime = True
        for p in primes:
            if p * p > i:
                break

            if i % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
            result += 2 ** (i - 1)

    return result
