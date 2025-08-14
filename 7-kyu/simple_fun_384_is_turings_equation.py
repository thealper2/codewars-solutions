def is_turing_equation(s):
    a, b = s.split('+')
    b, c = b.split('=')
    return int(a[::-1]) + int(b[::-1]) == int(c[::-1])
