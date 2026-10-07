def encode(string):
    return ''.join(
        c * 3
        for ch in string
        for c in format(ord(ch), '08b')
    )


def decode(bits):
    corrected = ''
    for i in range(0, len(bits), 3):
        triple = bits[i:i + 3]
        corrected += '1' if triple.count('1') >= 2 else '0'
    return ''.join(
        chr(int(corrected[i:i + 8], 2))
        for i in range(0, len(corrected), 8)
    )