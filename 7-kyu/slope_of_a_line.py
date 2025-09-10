def get_slope(p1, p2):
    if p1 == p2:
        return None
    
    a = p2[1] - p1[1]
    b = p2[0] - p1[0]
    if not b:
        return None
    
    return a / b
