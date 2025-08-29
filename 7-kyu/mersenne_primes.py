def lucas_lehmer(p):
    if p == 2:
        return True
    s = 4
    m = (1 << p) - 1
    for _ in range(p - 2):
        s = (s * s - 2) % m
        
    return s == 0

def valid_mersenne(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return lucas_lehmer(n)
