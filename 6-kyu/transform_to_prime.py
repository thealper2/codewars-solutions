def minimum_number(numbers):
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            
        return True
    
    total = sum(numbers)
    added = 0
    
    while not is_prime(total + added):
        added += 1
        
    return added