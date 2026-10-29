def sum_for_list(lst):
    primes = set()
    for x in lst:
        n = abs(x)
        d = 2
        while d * d <= n:
            if n % d == 0:
                primes.add(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            primes.add(n)
    
    result = []
    for p in sorted(primes):
        total = sum(x for x in lst if x % p == 0)
        result.append([p, total])
        
    return result