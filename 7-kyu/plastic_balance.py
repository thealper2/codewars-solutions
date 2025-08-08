def plastic_balance(lst):
    if len(lst) < 2:
        return lst
    
    while len(lst) >= 2:
        sum_sides = lst[0] + lst[-1]
        sum_rest = sum(lst[1:-1]) if len(lst) > 2 else 0
        if sum_sides == sum_rest:
            return lst
        
        lst = lst[1:-1]
        
    return []
