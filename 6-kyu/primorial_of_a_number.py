def is_prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def num_primorial(n):
    primes = []
    idx = 1
    result = 1
    while len(primes) < n:
        if is_prime(idx):
            result *= idx
            primes.append(idx)
            
        idx += 1
        
    return result
    