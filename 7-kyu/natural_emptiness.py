def rep_set(n):
    if n == 0:
        return []
    
    prev = rep_set(n - 1)
    return prev + [prev]
