def decode(r):
    i = 0
    while i < len(r) and r[i].isdigit():
        i += 1

    num = int(r[:i])
    encoded = r[i:]

    inv = None
    for x in range(26):
        if num * x % 26 == 1:
            inv = x
            break

    if inv is None:
        return "Impossible to decode"

    result = []
    for ch in encoded:
        y = ord(ch) - ord('a')
        x = y * inv % 26
        result.append(chr(x + ord('a')))

    return ''.join(result)