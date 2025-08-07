def save(sizes, hd): 
    n = len(sizes)
    count = 0
    total = 0
    
    for i in range(n):
        total += sizes[i]
        if total <= hd:
            count += 1
            
    return count
    
