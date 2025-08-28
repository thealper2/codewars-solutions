import math


def largest(n):
    if type(n) != int:
        return False
    
    if n <= 0:
        return False
    
    if n == 1:
        return 7
    
    lower = 10 ** (n - 1)
    upper = 10 ** n
    max_prime = float('-inf')
    for i in range(lower, upper):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
                
        if is_prime:
            max_prime = max(max_prime, i)
            
    return max_prime
