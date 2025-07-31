def is_valid(s):
    if not s:
        return False
    
    if not (s[0].isalpha() or s[0] == '_' or s[0] == '$'):
        return False
    
    for char in s[1:]:
        if not (char.isalpha() or char.isdigit() or char == '_' or char == '$'):
            return False
        
    return True
