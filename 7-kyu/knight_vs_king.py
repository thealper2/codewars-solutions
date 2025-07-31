def knight_vs_king(knight_position, king_position):
    knight_row, knight_col = knight_position
    king_row, king_col = king_position

    knight_col_num = ord(knight_col) - ord("A") + 1
    king_col_num = ord(king_col) - ord("A") + 1

    delta_row = abs(knight_row - king_row)
    delta_col = abs(knight_col_num - king_col_num)

    if (delta_row == 1 and delta_col == 2) or (delta_row == 2 and delta_col == 1):
        return "Knight"
    elif delta_row <= 1 and delta_col <= 1:
        return "King"
    else:
        return "None"
