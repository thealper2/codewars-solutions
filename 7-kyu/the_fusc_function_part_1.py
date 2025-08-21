def fusc(n):
    assert type(n) == int and n >= 0
    if n == 0:
        return 0
    a = 0
    b = 1
    s = bin(n)[2:]
    for char in s:
        if char == '0':
            b = a + b
        else:
            a = a + b
    return a
