def sum_diagonals(matrix):
    total = 0
    n = len(matrix)

    for i in range(n):
        total += matrix[i][i]
        total += matrix[n - i - 1][i]

    return total
