def sum_primes(lower, upper):
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
            
        return True
    
    if lower > upper:
        return 0
    
    total = 0
    for num in range(lower, upper + 1):
        if is_prime(num):
            total += num
            
    return total
