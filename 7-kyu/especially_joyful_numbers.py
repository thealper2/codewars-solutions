def number_joy(n):
    str_n = str(n)
    s = sum(map(int, str_n))
    if n % s != 0:
        return False
    
    s_r = int(str(s)[::-1])
    if s * s_r != n:
        return False
    
    return True
