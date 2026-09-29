def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    
    squares = []
    while lng > 0 and wdth > 0:
        if lng < wdth:
            lng, wdth = wdth, lng
            
        squares.append(wdth)
        lng -= wdth
        
    return squares