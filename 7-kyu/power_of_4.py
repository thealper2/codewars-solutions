def powerof4(n):
    if type(n) == str and not n.isdigit():
        return False
    
    if type(n) == str:
        n = int(n)
        
    if type(n) != int:
        return False
        
    i = 0
    while 4 ** i <= n:
        if 4 ** i == n:
            return True
        
        i += 1
        
    return False