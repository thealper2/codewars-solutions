def perfect_square(square):
    rows = square.split('\n')
    for c in square:
        if c not in ['.', '\n']:
            return False
        
    if not rows:
        return False
    
    width = len(rows[0])
    if width == 0:
        return False
    
    for row in rows:
        if len(row) != width:
            return False
        
    height = len(rows)
    return height == width
