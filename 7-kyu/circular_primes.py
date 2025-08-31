def circular_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        
        return True
    
    s = str(n)
    for i in range(len(s)):
        rotated = int(s[i:] + s[:i])
        if not is_prime(rotated):
            return False
        
    return True
