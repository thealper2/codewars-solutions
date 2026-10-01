def dashatize(n):
    if n < 0:
        n = -n

    s = str(n)
    result = []
    for ch in s:
        d = int(ch)
        if d % 2 == 1:
            if result and result[-1] != '-':
                result.append('-')

            result.append(ch)
            result.append('-')
        else:
            result.append(ch)

    out = ''.join(result).strip('-')
    return out