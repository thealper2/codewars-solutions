def construct_submatrix(matrix, rows_to_delete, cols_to_delete):
    n, m = len(matrix), len(matrix[0])
    result = []
    for i in range(n):
        new_row = []
        for j in range(m):
            if j not in cols_to_delete:
                new_row.append(matrix[i][j])
                
        if i not in rows_to_delete:
            result.append(new_row)
        
    return result
