def is_happy(n):
    result = 0
    seen = set()
    
    while n != 1:
        result = 0
        while n > 0:
            digit = n % 10
            result += digit * digit
            n //= 10
            
        n = result
        if n in seen:
            return False
        
        seen.add(n)
        
    return True
