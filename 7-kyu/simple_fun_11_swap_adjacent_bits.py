def swap_adjacent_bits(n):
    binary_n = str(bin(n))[2:]
    l = len(binary_n)
    if l % 2 == 1:
        binary_n = '0' + binary_n
        l += 1
        
    result = []
    for i in range(0, l - 1, 2):
        result.append(binary_n[i:i+2][::-1])
        
    return int(''.join(result), 2)
