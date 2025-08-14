def square_up(n):
    result = []
    for i in range(1, n + 1):
        result += [0] * (n - i)
        result += list(range(i, 0, -1))
    return result
