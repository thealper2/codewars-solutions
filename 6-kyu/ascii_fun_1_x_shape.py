def x(n):
    result = [['□'] * n for _ in range(n)]
    print(result)
    for i in range(n):
        result[i][i] = '■'
        result[i][n - i - 1] = '■'

    return '\n'.join(''.join(row) for row in result)