import math


def odd_not_prime(n):
    count = 0
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            is_prime = True
            if i == 1:
                is_prime = False
            else:
                for j in range(2, int(math.sqrt(i)) + 1):
                    if i % j == 0:
                        is_prime = False
                        break
                        
            if not is_prime:
                count += 1
                
    return count
