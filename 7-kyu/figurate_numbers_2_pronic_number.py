def is_pronic(n):
    if n < 0:
        return False
    
    for i in range(n + 1):
        if i * (i + 1) == n:
            return True
        
    return False
