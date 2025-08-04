def least_larger(a, i): 
    target = a[i]
    candidates = []
    for num in a:
        if num > target:
            candidates.append(num)
            
    if not candidates:
        return -1
    
    min_larger = min(candidates)
    return a.index(min_larger)