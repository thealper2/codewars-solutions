def toggle_bit(n, p):
    return n ^ (1 << p)

def set_bit(n, p):
    return n | (1 << p)
    
def clear_bit(n, p):
    return n & ~(1 << p)
    
def is_bit_set(n, p):
    return (n >> p) & 1 == 1
    
def set_multiple_bits(n, mask):
    return n | mask
    
def clear_multiple_bits(n, mask):
    return n & ~mask

def toggle_multiple_bits(n, mask):
    return n ^ mask
