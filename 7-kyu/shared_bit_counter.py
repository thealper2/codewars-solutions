def shared_bits(a, b):
    count = 0
    while a > 0 and b > 0:
        d_a = a % 2
        a //= 2
        
        d_b = b % 2
        b //= 2
        
        if d_a == 1 and d_b == 1:
            count += 1
            
    return count >= 2