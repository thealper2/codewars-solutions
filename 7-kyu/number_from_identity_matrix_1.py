def soln(n):
    result = 1
    for i in range(1, n):
        result += 2 ** (i * (n+1))

    return result
