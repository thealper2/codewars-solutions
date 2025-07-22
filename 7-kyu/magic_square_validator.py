def is_magical(square):
    lines = [
        # Rows
        [square[0], square[1], square[2]],
        [square[3], square[4], square[5]],
        [square[6], square[7], square[8]],
        # Columns
        [square[0], square[3], square[6]],
        [square[1], square[4], square[7]],
        [square[2], square[5], square[8]],
        # Diagonals
        [square[0], square[4], square[8]],
        [square[2], square[4], square[6]]
    ]
    
    return all(sum(line) == 15 for line in lines)