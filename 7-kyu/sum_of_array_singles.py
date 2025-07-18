def repeats(arr):
    seen = set()
    total = 0
    
    for i in arr:
        if i not in seen:
            total += i 
            seen.add(i)
        else:
            total -= i
            
    return total
