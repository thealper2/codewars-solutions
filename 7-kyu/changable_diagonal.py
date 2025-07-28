def matrix_diagonal(matrix, value):
    if not matrix:
        return 0
    
    n = len(matrix)
    diagonal = []
    if value > 0:
        row = value
        col = 0
        while row < n and col < n:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
    elif value < 0:
        row = 0
        col = -value
        while row < n and col < n:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
    else:
        for i in range(n):
            diagonal.append(matrix[i][i])
    
    return sum(diagonal)