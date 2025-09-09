def cool_string(s): 
    n = len(s)
    if not s.isalpha():
        return False
    
    for i in range(n - 1):
        a, b = s[i], s[i + 1]
        if a.isalpha() and b.isalpha():
            a_l = a.islower()
            b_l = b.islower()
            if a_l == b_l:
                return False
        
    return True
