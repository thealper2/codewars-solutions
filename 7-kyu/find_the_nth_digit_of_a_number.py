def find_digit(num, nth):
    if nth <= 0:
        return -1
    
    if num < 0:
        num = -num
    
    i = 0
    while 10 ** i <= num:
        d = num // 10 ** i % 10
        if i + 1 == nth:
            return d
        
        i += 1
        
    return 0