def spot_diff(s1, s2):
    if s1 == s2:
        return []
    
    idx = 0
    result = []
    for a, b in zip(s1, s2):
        if a != b:
            result.append(idx)
            
        idx += 1
    
    return result
