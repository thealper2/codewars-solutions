def sum_no_duplicates(l):
    total = 0
    for c in l:
        if l.count(c) == 1:
            total += c
            
    return total
