def chess_board(rows, columns):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if (i + j) % 2 == 0:
                row.append("O")
            else:
                row.append("X")
                
        board.append(row)
        
    return board