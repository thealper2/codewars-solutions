def duplicate_elements(m, n):
    if not m or not n:
        return False
    
    set_m = set(m)
    for val in n:
        if val in set_m:
            return True
        
    return False
