import re

def decode_bits(bits):
    bits = bits.strip('0')
    if not bits:
        return ''

    ones = [len(m) for m in re.findall(r'1+', bits)]
    zeros = [len(m) for m in re.findall(r'0+', bits)]
    candidates = ones + zeros
    unit = min(candidates)

    result = []
    for m in re.finditer(r'1+|0+', bits):
        run = m.group(0)
        n = len(run) // unit
        if run[0] == '1':
            result.append('.' if n == 1 else '-')
        else:
            if n == 1:
                result.append('')
            elif n == 3:
                result.append(' ')
            else:
                result.append('   ')
                
    return ''.join(result)


def decode_morse(morse_code):
    return ' '.join(
        ''.join(MORSE_CODE[c] for c in word.split(' '))
        for word in morse_code.strip().split('   ')
    )