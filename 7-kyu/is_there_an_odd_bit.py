def any_odd(x):
    i = 0
    while x > 0:
        i += 1
        
        if i % 2 == 0 and x % 2 == 1:
            return True
        
        x //= 2
        
    return 0