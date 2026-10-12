def cat_mouse(x,j):
    if 'C' not in x or 'D' not in x or 'm' not in x:
        return 'boring without all three'
    
    c = x.index('C')
    m = x.index('m')
    d = x.index('D')
    
    if abs(c - m) <= j:
        lo, hi = min(c, m), max(c, m)
        if lo < d < hi:
            return 'Protected!'
        
        return 'Caught!'
    
    return 'Escaped!'