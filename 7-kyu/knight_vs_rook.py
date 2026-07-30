def knight_vs_rook(knight, rook):
    k_row, k_col = knight
    r_row, r_col = rook
    
    k_col = ord(k_col) - 65
    r_col = ord(r_col) - 65
    
    if k_row == r_row or k_col == r_col:
        return 'Rook'
    
    row_diff = abs(k_row - r_row)
    col_diff = abs(k_col - r_col)
    
    if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
        return 'Knight'
    
    return 'None'
