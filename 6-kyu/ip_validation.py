def is_valid_IP(strng):
    parts = strng.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        if len(part) == 3 and (part[0] == ' ' or part[0] == '0'):
            return False
        
        if len(part) == 2 and part[0] == '0':
            return False
        
        if int(part) < 0 or int(part) > 255:
            return False
        
    return True