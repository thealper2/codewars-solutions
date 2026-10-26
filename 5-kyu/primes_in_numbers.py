def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                n //= d
                count += 1
                
            factors.append((d, count))
        d += 1
        
    if n > 1:
        factors.append((n, 1))
        
    parts = []
    for p, e in factors:
        if e == 1:
            parts.append(f"({p})")
        else:
            parts.append(f"({p}**{e})")
            
    return ''.join(parts)