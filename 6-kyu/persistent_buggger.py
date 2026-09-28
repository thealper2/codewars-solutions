def persistence(n):
    count = 0
    while n >= 10:
        new_n = 1
        while n > 0:
            new_n *= n % 10
            n //= 10
        
        count += 1
        n = new_n
        
    return count