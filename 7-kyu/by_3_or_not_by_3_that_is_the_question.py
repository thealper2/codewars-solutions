def divisible_by_three(st): 
    s = sum(map(int, st))
    while s >= 3:
        s -= 3
        
    return s == 0
