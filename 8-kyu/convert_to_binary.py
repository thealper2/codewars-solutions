def to_binary(n):
    i = n
    result = []
    while i >= 1:
        a = i % 2
        i = i // 2
        result[0:0] = str(a)

    return int("".join(result))
