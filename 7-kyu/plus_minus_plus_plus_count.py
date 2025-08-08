def catch_sign_change(lst):
    n = len(lst)
    count = 0
    
    for i in range(1, n):
        if (lst[i] < 0 and lst[i - 1] >= 0) or (lst[i] >= 0 and lst[i - 1] < 0):
            count += 1
            
    return count
