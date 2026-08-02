def split_by_mask(strng, mask):
    n = len(strng)
    if n != sum(mask):
        return None
    
    result = []
    i = 0
    
    for m in mask:
        sub = strng[i:i+m]
        result.append(sub)
        i += m
    
    return result
