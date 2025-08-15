def size_to_number(size):
    if not size:
        return None
    
    valid_chars = {'x', 's', 'm', 'l'}
    for char in size:
        if char not in valid_chars:
            return None
    
    if len(size) == 0:
        return None
    
    base = size[-1]
    if base not in {'s', 'm', 'l'}:
        return None
    
    modifiers = size[:-1]
    for mod in modifiers:
        if mod != 'x':
            return None
    
    if len(size) > 1 and size[-2] in {'s', 'm', 'l'}:
        return None
    
    if base == 's':
        base_num = 36
        num = base_num - 2 * len(modifiers)
        return num
    elif base == 'm':
        if len(modifiers) > 0:
            return None
        return 38
    elif base == 'l':
        base_num = 40
        num = base_num + 2 * len(modifiers)
        return num
    else:
        return None
