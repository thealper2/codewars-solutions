def mystery(n):
    if n <= 0:
        return []

    result = []
    for i in range(1, n + 1, 2):
        if n % i == 0:
            result.append(i)

    return result
