def is_zero_balanced(arr):
    if not arr:
        return False
    
    s = 0
    for item in arr:
        if -item in arr:
            s += item
        else:
            return False
        
    return s == 0
