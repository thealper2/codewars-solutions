def get_matrix(n):
    matrix = []

    for i in range(n):
        row = [0 for _ in range(n)]
        row[i] = 1
        matrix.append(row)

    return matrix
