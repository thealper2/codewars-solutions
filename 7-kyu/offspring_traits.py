def bear_fur(bears):
    a, b = sorted(bears)
    if a == b:
        return a
    
    if a == 'black' and b == 'brown':
        return 'dark brown'
    
    if a == 'black' and b == 'white':
        return 'grey'
    
    if a == 'brown' and b == 'white':
        return 'light brown'
    
    return 'unknown'
