def skiponacci(n):
    if n == 0:
        return ""

    result = []
    a, b = 0, 1

    for i in range(1, n + 1):
        if i % 2 == 1:
            result.append(str(b))
        else:
            result.append("skip")
        a, b = b, a + b

    return " ".join(result)
