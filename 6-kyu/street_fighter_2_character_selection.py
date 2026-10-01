def street_fighter_selection(fighters, initial_position, moves):
    row, col = initial_position
    n_rows = len(fighters)
    n_cols = len(fighters[0])
    hovered = []
    for move in moves:
        if move == 'up':
            row = max(0, row - 1)
        elif move == 'down':
            row = min(n_rows - 1, row + 1)
        elif move == 'left':
            col = (col - 1) % n_cols
        elif move == 'right':
            col = (col + 1) % n_cols

        hovered.append(fighters[row][col])

    return hovered