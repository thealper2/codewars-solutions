def not_primes(a, b):
    sieve = bytearray([1]) * b
    if b > 0: sieve[0] = 0
    if b > 1: sieve[1] = 0
    for i in range(2, int(b**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    pd = set('2357')
    return [n for n in range(max(a, 10), b)
            if not sieve[n] and all(c in pd for c in str(n))]