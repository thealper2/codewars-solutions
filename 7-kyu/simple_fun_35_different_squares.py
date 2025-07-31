def different_squares(matrix):
    squares = set()
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            square = (
                matrix[i][j],
                matrix[i][j + 1],
                matrix[i + 1][j],
                matrix[i + 1][j + 1],
            )
            squares.add(square)
    return len(squares)
