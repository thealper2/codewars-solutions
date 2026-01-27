def find_saddle_points(matrix):
    if not matrix:
        return []
    
    n = len(matrix)
    m = len(matrix[0])
    
    row_mins = []
    for i in range(n):
        row = matrix[i]
        min_val = min(row)
        row_mins.append((i, [j for j, val in enumerate(row) if val == min_val], min_val))
    
    col_maxs = []
    for j in range(m):
        col_vals = [matrix[i][j] for i in range(n)]
        max_val = max(col_vals)
        col_maxs.append((j, [i for i, val in enumerate(col_vals) if val == max_val], max_val))
    
    saddle_points = []
    for i, min_cols, min_val in row_mins:
        for j in min_cols:
            col_j = col_maxs[j]
            if i in col_j[1] and matrix[i][j] == col_j[2]:
                saddle_points.append((i, j))
    
    return saddle_points
