def encode_cd(n):
    bits = bin(n)[2:].zfill(8)[::-1]
    result = ['P']
    for bit in bits:
        if bit == '1':
            result.append('L' if result[-1] == 'P' else 'P')
        else:
            result.append(result[-1])
            
    return ''.join(result)
