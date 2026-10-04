def is_valid_coordinates(coordinates):
    for c in coordinates:
        if c not in ' 0123456789-.,':
            return False
    
    parts = coordinates.split(',')
    if len(parts) != 2:
        return False
    
    x, y = parts[0], parts[1]
    x = x.strip()
    y = y.strip()
    
    if x.count('.') > 1 or y.count('.') > 1:
        return False
    
    if ' ' in x or ' ' in y:
        return False
    
    if '_' in x or '_' in y:
        return False
    
    x = float(x)
    y = float(y)

    if x < -90 or x > 90:
        return False
    
    if y < -180 or y > 180:
        return False
    
    return True