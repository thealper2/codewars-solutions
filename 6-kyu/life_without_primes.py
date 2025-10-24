def is_prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
        
    return True


def has_only_allowed_digits(num):
    allowed_digits = {'0', '1', '4', '6', '8', '9'}
    digits = set(str(num))
    return digits.issubset(allowed_digits)

def solve(n):
    sequence = []
    num = 1
    while len(sequence) <= n:
        if has_only_allowed_digits(num) and not is_prime(num):
            sequence.append(num)
            
        num += 1
        
    return sequence[-1]
