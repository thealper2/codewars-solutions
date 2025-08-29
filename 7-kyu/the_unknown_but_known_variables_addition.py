def the_var(s):
    a, b = s.split('+')
    return (ord(a) - ord('a') + 1) + (ord(b) - ord('a') + 1)
