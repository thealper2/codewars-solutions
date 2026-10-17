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

def solve(a, b):
    primes = []
    n = 2
    total_digits = 0
    
    while total_digits < a + b:
        if is_prime(n):
            primes.append(str(n))
            total_digits += len(str(n))
        
        n += 1
        
    result = ''.join(primes)
    return result[a:a + b]