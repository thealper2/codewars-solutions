def rat_at(n):
    a, b = 1, 1
    for bit in bin(n + 1)[3:]:
        if bit == '0':
            b = a + b
        else:
            a = a + b
            
    return (a, b)


def index_of(a, b):
    bits = []
    while (a, b) != (1, 1):
        if a < b:
            bits.append('0')
            b -= a
        else:
            bits.append('1')
            a -= b
            
    return int('1' + ''.join(reversed(bits)), 2) - 1
