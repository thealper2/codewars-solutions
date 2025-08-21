import math


def is_prime(i):
    if i < 2:
        return False
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                return False
            
    return True


def sexy_prime(x, y):
    if not is_prime(x) or not is_prime(y):
        return False
    
    if abs(x - y) != 6:
        return False
    
    return True
