def hop_across(lst):
    pos1 = 0
    steps1 = 0
    n = len(lst)
    while pos1 < n:
        steps1 += 1
        pos1 += lst[pos1]
        
    pos2 = 0
    steps2 = 0
    r_lst = lst[::-1]
    while pos2 < n:
        steps2 += 1
        pos2 += r_lst[pos2]
        
    return steps1 + steps2
