def maximum_seating(lst):
    n = len(lst)
    cnt = 0
    for i in range(n):
        if lst[i] == 0:
            l1 = (i - 1 < 0 or lst[i - 1] == 0)
            l2 = (i - 2 < 0 or lst[i - 2] == 0)
            r1 = (i + 1 >= n or lst[i + 1] == 0)
            r2 = (i + 2 >= n or lst[i + 2] == 0)
            if l1 and l2 and r1 and r2:
                lst[i] = 1
                cnt += 1
                
    return cnt
