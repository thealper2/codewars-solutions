def show_bits(n):
    result = []
    for i in range(31, -1, -1):
        bit = (n >> i) & 1
        result.append(bit)
        
    return result
