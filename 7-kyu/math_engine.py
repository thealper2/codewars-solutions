def math_engine(arr):
    if not isinstance(arr, list):
        return 0
    
    if not arr:
        return 1
    
    p = 1
    s = 0
    for i in arr:
        if i < 0:
            s += i
        else:
            p *= i
            
    return p + s
