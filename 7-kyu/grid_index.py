def grid_index(grid, indexes):
    n = len(grid)
    result = ''
    for index in indexes:
        a = (index - 1) // n
        b = (index - 1) % n
        result += grid[a][b]
        
    return result
