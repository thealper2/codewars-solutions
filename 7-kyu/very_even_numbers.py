def is_very_even_number(n):
    while n >= 10:
        digit_sum = 0
        while n:
            digit_sum += n % 10
            n //= 10
            
        n = digit_sum
        
    return n % 2 == 0
