def possible_positions(pos):
    col, row = pos[0], int(pos[1])
    moves = []
    directions = [
        (-2,-1), (-2,1),
        (-1,-2), (-1,2),
        (1,-2), (1,2),
        (2,-1), (2,1)
    ]
    for dc, dr in directions:
        new_col = chr(ord(col) + dc)
        new_row = row + dr
        if 'a' <= new_col <= 'h' and 1 <= new_row <= 8:
            moves.append(new_col + str(new_row))
    
    return sorted(moves)
