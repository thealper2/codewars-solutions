def max_land_value(grid : list[list[int]]) -> int :
    rows = len(grid)
    cols = len(grid[0])

    if rows % 2 == 0:
        top_rows = range(0, rows // 2)
        bottom_rows = range(rows // 2, rows)
    else:
        top_rows = range(0, rows // 2)
        bottom_rows = range(rows // 2 + 1, rows)

    if cols % 2 == 0:
        left_cols = range(0, cols // 2)
        right_cols = range(cols // 2, cols)
    else:
        left_cols = range(0, cols // 2)
        right_cols = range(cols // 2 + 1, cols)

    top_left = sum(grid[i][j] for i in top_rows for j in left_cols)
    top_right = sum(grid[i][j] for i in top_rows for j in right_cols)
    bottom_left = sum(grid[i][j] for i in bottom_rows for j in left_cols)
    bottom_right = sum(grid[i][j] for i in bottom_rows for j in right_cols)

    return max(top_left, top_right, bottom_left, bottom_right)
