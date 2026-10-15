def code(strng):
    result = []
    for ch in strng:
        d = int(ch)
        if d == 0:
            bits = '0'
        else:
            bits = bin(d)[2:]

        k = len(bits)
        result.append('0' * (k - 1) + '1' + bits)

    return ''.join(result)

def decode(strng):
    result = []
    i = 0
    n = len(strng)
    while i < n:
        zeros = 0
        while i < n and strng[i] == '0':
            zeros += 1
            i += 1

        i += 1
        k = zeros + 1
        bits = strng[i:i + k]
        i += k
        result.append(str(int(bits, 2)))

    return ''.join(result)