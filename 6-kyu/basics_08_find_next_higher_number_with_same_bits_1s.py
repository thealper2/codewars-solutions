def next_higher(n):
    c = n
    c0 = 0
    c1 = 0
    while c != 0 and (c & 1) == 0:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    p = c0 + c1
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n