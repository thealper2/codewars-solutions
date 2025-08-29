def generate_primes(x):
    if x < 2:
        return []
    
    sieve = [True] * (x + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(x**0.5) + 1):
        if sieve[i]:
            sieve[i*i : x+1 : i] = [False] * len(sieve[i*i : x+1 : i])
    
    return [i for i, is_prime in enumerate(sieve) if is_prime]
