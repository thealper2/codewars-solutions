def swap(matrix, row1, row2, *cols):
    if row1 < 0 or row1 >= len(matrix) or row2 < 0 or row2 >= len(matrix):
        return matrix
    
    for col in cols:
        if col < 0 or col >= len(matrix[0]):
            return matrix
    
    for col in cols:
        matrix[row1][col], matrix[row2][col] = matrix[row2][col], matrix[row1][col]
    
    return matrix
