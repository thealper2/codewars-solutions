def password(st):
    c1, c2, c3, c4 = False, False, False, False
    
    if len(st) >= 8:
        c4 = 1
        
    for c in st:
        if 65 <= ord(c) <= 90:
            c1 = 1
            
        elif 97 <= ord(c) <= 122:
            c2 = 1
            
        elif c.isdigit():
            c3 = 1
            
    return bool(c1 & c2 & c3 & c4)
