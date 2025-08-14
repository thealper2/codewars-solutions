def increasing_number(x, n):
    i = 0
    while i < n:
        x += 1
        if x % (i + 1) == 0:
            i += 1
            
    return x - n
            
