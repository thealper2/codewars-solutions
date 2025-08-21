def next_numb(val):
    max_val = 9876543210
    if val >= max_val:
        return "There is no possible number that fulfills those requirements"
    
    n = val + 1
    while n <= max_val:
        s = str(n)
        if len(s) != len(set(s)):
            n += 1
            continue
        
        if n % 2 != 1:
            n += 1
            continue
        
        if n % 3 != 0:
            n += 1
            continue
        
        return n
    
    return "There is no possible number that fulfills those requirements"
