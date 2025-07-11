import random

def is_prime(num):
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if num % p == 0:
            return num == p
        
    d = num - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
        
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= num:
            continue
        
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    
    return True

def next_prime(n):
    if n < 2:
        return 2
    
    candidate = n + 1
    
    if candidate % 2 == 0:
        candidate += 1
    
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 2