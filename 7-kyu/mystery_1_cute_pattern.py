def cute_pattern(tiles):
    matrix = [list(row) for row in tiles.split('\n')]
    n = len(matrix)
    
    for i in range(n - 1):
        for j in range(n - 1):
            a = matrix[i][j]
            b = matrix[i][j+1]
            c = matrix[i+1][j]
            d = matrix[i+1][j+1]
            if a == b == c == d:
                return False
    return True
