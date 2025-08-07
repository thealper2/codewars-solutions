def candies(lst):
    if len(lst) <= 1:
        return -1
    
    max_candy = max(lst)
    total = 0
    for candy in lst:
        total += max_candy - candy
        
    return total
