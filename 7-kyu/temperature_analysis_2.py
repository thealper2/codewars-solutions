def close_to_zero(t):
    if not t:
        return 0
    
    values = map(int, t.split())
    min_dist = float('inf')
    for value in values:
        if value == 0:
            return 0
        
        if abs(value) < abs(min_dist):
            min_dist = value
        elif abs(value) == abs(min_dist):
            if value > min_dist:
                min_dist = value
                
    return min_dist
        
