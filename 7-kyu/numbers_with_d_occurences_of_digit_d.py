def is_dd(n):
    str_n = str(n)
    for c in str_n:
        if str_n.count(c) == int(c):
            return True
        
    return False
