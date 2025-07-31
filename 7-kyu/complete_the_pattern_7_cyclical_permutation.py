def pattern(n):
    if n <= 0:
        return ""

    result = []
    for i in range(1, n + 1):
        p = "".join([str(_) for _ in range(i, n + 1)])
        for j in range(1, i):
            p += str(j)

        result.append(p)

    return "\n".join(result)
