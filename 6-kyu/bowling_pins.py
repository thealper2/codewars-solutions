def bowling_pins(arr : list[int]) -> str:
    layout = {
        7: (0, 0), 8: (0, 2), 9: (0, 4), 10: (0, 6),
        4: (1, 1), 5: (1, 3), 6: (1, 5),
        2: (2, 2), 3: (2, 4),
        1: (3, 3),
    }

    removed = set(arr)
    grid = [[' '] * 7 for _ in range(4)]
    for pin, (r, c) in layout.items():
        if pin not in removed:
            grid[r][c] = 'I'

    return '\n'.join(''.join(row) for row in grid)