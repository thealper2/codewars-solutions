def knight_vs_bishop(knight_position, bishop_position):
    row1, col1 = knight_position
    row2, col2 = bishop_position
    
    col1 = ord(col1) - ord('A') + 1
    col2 = ord(col2) - ord('A') + 1
    
    delta_row = abs(row1 - row2)
    delta_col = abs(col1 - col2)
    
    if (delta_row == 1 and delta_col == 2) or (delta_row == 2 and delta_col == 1):
        return "Knight"
    elif delta_row == delta_col:
        return "Bishop"
    else:
        return "None"