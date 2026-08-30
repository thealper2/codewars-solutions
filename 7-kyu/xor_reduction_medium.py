def xor_0_to_n(n):
    if n < 0:
        return 0
    
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n + 1
    else:
        return 0
    
def xor_reduction(m, n):
    return xor_0_to_n(n) ^ xor_0_to_n(m - 1)