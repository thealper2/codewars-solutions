def is_smooth(n):
    max_prime = 1
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            max_prime = i
            n //= i
        i += 2
        
    if n > 2:
        max_prime = n
    
    if max_prime == 2:
        return "power of 2"
    elif max_prime == 3:
        return "3-smooth"
    elif max_prime == 5:
        return "Hamming number"
    elif max_prime == 7:
        return "humble number"
    else:
        return "non-smooth"
