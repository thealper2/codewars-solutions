def whitespace_number(n):
    if n == 0:
        return ' \n'
    
    sign = ' ' if n > 0 else '\t'
    magnitude = abs(n)
    bits = bin(magnitude)[2:]
    encoded = ''.join(' ' if b == '0' else '\t' for b in bits)
    return sign + encoded + '\n'