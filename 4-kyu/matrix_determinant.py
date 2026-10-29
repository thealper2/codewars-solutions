def determinant(matrix):
    if isinstance(matrix, (int, float)):
        return matrix
    if len(matrix) == 1:
        return matrix[0][0]
    
    det_func = lambda f, mat: mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1] if all(
        [len(row) == 2 for row in mat]) and len(mat) == 2 else sum([
        (1 - 2*(ind%2))*(row[0])*f(f, [[el for el in new_row[1:]] 
        for row_ind, new_row in enumerate(mat) if row_ind != ind]) 
        for ind, row in enumerate(mat)
    ])
    det = lambda mat: det_func(det_func, mat)
    return det(matrix)