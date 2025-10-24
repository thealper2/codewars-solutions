import math

def lucky_sevens(grid):
    is_perfect_cube = lambda x: round(x ** (1 / 3)) ** 3 == x
    rows, cols = len(grid), len(grid[0])
    result = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 7:
                surrounding_sum = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if (0 <= ni < rows and 0 <= nj < cols and isinstance(grid[ni][nj], (int, float)) and grid[ni][nj] != 'x'):
                        surrounding_sum += grid[ni][nj]
                        
                if surrounding_sum > 0 and is_perfect_cube(surrounding_sum):
                    result += 1
                    
    return result
