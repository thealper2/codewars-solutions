def convert(input, source, target):
    base_src = len(source)
    value = 0
    for ch in input:
        value = value * base_src + source.index(ch)

    base_tgt = len(target)
    if value == 0:
        return target[0]

    digits = []
    while value > 0:
        digits.append(target[value % base_tgt])
        value //= base_tgt

    return ''.join(reversed(digits))