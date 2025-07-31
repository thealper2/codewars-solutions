def even_chars(st):
    n = len(st)

    if n < 2 or n > 100:
        return "invalid string"

    result = []
    for i in range(1, n, 2):
        result.append(st[i])

    return result
