def substring_test(s1, s2):
    if not s1 or not s2:
        return False
    
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) <= len(s2):
        for i in range(0, len(s1) - 1):
            if s1[i:i+2] in s2:
                return True
    else:
        for i in range(0, len(s2) - 1):
            if s2[i:i+2] in s1:
                return True
            
    return False