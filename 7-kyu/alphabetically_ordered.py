def alphabetic(s):
    if not s:
        return True
    
    n = len(s)
    prev = s[0]
    for i in range(1, n):
        if prev and ord(s[i]) < ord(prev):
            return False
    
        prev = s[i]
        
    return True
