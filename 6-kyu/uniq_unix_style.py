def uniq(seq):
    result = []
    for x in seq:
        if not result or result[-1] != x:
            result.append(x)

    return result