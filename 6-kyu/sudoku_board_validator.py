def validate_sudoku(board):
    expected = set(range(1, 10))
    
    for row in board:
        if set(row) != expected:
            return False
        
    for c in range(9):
        if set(board[r][c] for r in range(9)) != expected:
            return False
        
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            block = set(
                board[br + i][bc + j]
                for i in range(3)
                for j in range(3)
            )
            if block != expected:
                return False
            
    return True