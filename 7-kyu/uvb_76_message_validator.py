import re

def validate(message):
    parts = message.split()
    
    if len(parts) != 8:
        return False
    
    if parts[0] != "MDZHB":
        return False
    
    if not re.fullmatch(r'^\d{2}$', parts[1]):
        return False
    
    if not re.fullmatch(r'^\d{3}$', parts[2]):
        return False
    
    if not re.fullmatch(r'^[A-Z]+$', parts[3]):
        return False
    
    for part in parts[4:8]:
        if not re.fullmatch(r'^\d{2}$', part):
            return False
    
    return True