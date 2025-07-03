def hamming_weight(x):
    c = 0
    while x >= 1:
        if x % 2 == 1:
            c += 1
        x //= 2
    
    return c