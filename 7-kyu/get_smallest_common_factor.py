def scf(arr):
    if not arr:
        return 1
    
    min_val = min(arr)
    result = 2
    factors = []
    for i in range(2, min_val + 1):
        is_factor = True
        for item in arr:
            if item % i != 0:
                is_factor = False
                
        if is_factor:
            factors.append(i)
            
    return min(factors) if factors else 1
            
