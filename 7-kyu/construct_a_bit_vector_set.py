def sort_by_bit(seq): 
    result = 0
    for index in seq:
        if 0 <= index < 32:
            result |= 1 << index
            
    return result