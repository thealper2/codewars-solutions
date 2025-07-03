def is_cleanly_nested(arr):
    if not arr:
        return True
    
    all_empty = all(len(elem) == 0 for elem in arr)
    all_non_empty = all(len(elem) > 0 for elem in arr)
    
    if not (all_empty or all_non_empty):
        return False
    
    for elem in arr:
        if len(elem) > 0:
            if not is_cleanly_nested(elem):
                return False
    
    return True
