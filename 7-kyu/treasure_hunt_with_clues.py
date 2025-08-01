def find_treasure(grid, start_row, start_col):
    n = len(grid)
    current_row, current_col = start_row - 1, start_col - 1
    
    while True:
        value = grid[current_row][current_col]
        expected_value = (current_row + 1) * 10 + (current_col + 1)
        if value == expected_value:
            return value

        next_row = value // 10 - 1
        next_col = value % 10 - 1
        current_row, current_col = next_row, next_col
