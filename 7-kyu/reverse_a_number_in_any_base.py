def reverse_number(n, b):
    if b == 1:
        return n
    digits = []
    if n == 0:
        digits = [0]
    else:
        while n > 0:
            digits.append(n % b)
            n = n // b
            
    reversed_num = 0
    for i, digit in enumerate(digits):
        reversed_num += digit * (b ** (len(digits) - 1 - i))
    
    return reversed_num
        
