def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)
    
    if heads < 0 or legs < 0:
        return "No solutions"
    
    # x = (legs - 2y) / 4
    # y = (4 * heads - legs) / 2
    y = (4 * heads - legs) / 2
    x = (legs - 2 * y) / 4
    if x.is_integer() and y.is_integer():
        if x >= 0 and y >= 0:
            return (y, x)
        else:
            return "No solutions"
    else:
        return "No solutions"