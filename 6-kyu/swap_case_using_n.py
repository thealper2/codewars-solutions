def swap(s,n):
    if n == 0:
        return s
    
    bits = bin(n)[2:]
    bit_len = len(bits)
    result = []
    bit_pos = 0
    for ch in s:
        if ch.isalpha():
            bit = bits[bit_pos % bit_len]
            bit_pos += 1
            if bit == '1':
                result.append(ch.swapcase())
            else:
                result.append(ch)
        else:
            result.append(ch)
            
    return ''.join(result)