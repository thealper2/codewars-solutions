def stray(arr):
    for c in set(arr):
        if arr.count(c) == 1:
            return c
        
    return -1
