def int_diff(lst, n):
    total = 0
    l = len(lst)
    for i in range(l):
        for j in range(i + 1, l):
            if abs(lst[i] - lst[j]) == n:
                total += 1
                
    return total
