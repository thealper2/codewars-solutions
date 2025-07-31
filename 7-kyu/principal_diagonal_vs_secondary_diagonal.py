def diagonal(matrix):
    n = len(matrix)
    principal_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        principal_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][n - 1 - i]

    if principal_diagonal > secondary_diagonal:
        return "Principal Diagonal win!"

    elif secondary_diagonal > principal_diagonal:
        return "Secondary Diagonal win!"

    else:
        return "Draw!"
