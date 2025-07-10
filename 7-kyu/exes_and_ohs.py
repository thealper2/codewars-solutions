def xo(s):
    s = s.replace('X', 'x')
    s = s.replace('O', 'o')
    return s.count('x') == s.count('o')