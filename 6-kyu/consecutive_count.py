def get_consective_items(items, key): 
    max_l = 0
    curr_l = 0
    items = str(items)
    key = str(key)
    
    for item in items:
        if item == key:
            curr_l += 1
            max_l = max(max_l, curr_l)
        else:
            curr_l = 0
            
    return max_l
