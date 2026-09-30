def move_zeros(lst):
    idx = 0
    n = len(lst)
    
    for num in lst:
        if num != 0:
            lst[idx] = num
            idx += 1
            
    for i in range(idx, n):
        lst[i] = 0
        
    return lst