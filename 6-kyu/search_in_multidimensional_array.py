def locate(seq: list, value) -> bool: 
    for item in seq:
        if item == value:
            return True
        
        elif isinstance(item, list):
            if locate(item, value):
                return True
            
    return False
