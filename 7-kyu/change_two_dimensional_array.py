def matrix(matrix): 
    modified_matrix = [row[:] for row in matrix]
    n = len(modified_matrix)
    for i in range(n):
        if modified_matrix[i][i] < 0:
            modified_matrix[i][i] = 0
        else:
            modified_matrix[i][i] = 1
            
    return modified_matrix
