def step(g, m, n):
    def is_prime(num):
        if num < 2:
            return False
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            
        return True
    
    for num in range(m, n - g + 1):
        if is_prime(num) and is_prime(num + g):
            return [num, num + g]
        
    return None