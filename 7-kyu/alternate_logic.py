def alt_or(lst):
    if not lst:
        return None
    
    result = lst[0]
    for item in lst[1:]:
        result = result | item
        
    return result
