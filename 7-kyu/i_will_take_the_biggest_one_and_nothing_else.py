def max_int_chain(n):
    if n < 2:
        return -1
    
    l = n // 2
    r = (n + 1) // 2
    
    if l == r:
        l -= 1
        r += 1
    
    if l + r != n or l * r <= n:
        return -1
    
    return l * r
