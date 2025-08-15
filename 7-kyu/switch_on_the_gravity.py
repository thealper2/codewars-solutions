def switch_gravity(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed = [[matrix[row][col] for row in range(rows)] for col in range(cols)]
    for i in range(cols):
        column = transposed[i]
        num_blocks = column.count('#')
        new_column = ['-'] * (rows - num_blocks) + ['#'] * num_blocks
        transposed[i] = new_column
    
    result = [[transposed[col][row] for col in range(cols)] for row in range(rows)]
    return result
