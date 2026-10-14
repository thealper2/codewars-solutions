def display_board(board, width):
    rows = []
    for i in range(0, len(board), width):
        row = board[i:i + width]
        rows.append(' ' + ' | '.join(row) + ' ')
        
    separator = '\n' + '-' * len(rows[0]) + '\n'
    return separator.join(rows)