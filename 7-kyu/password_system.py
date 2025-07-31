import math


def help_zoom(grid):
    length = len(grid)
    n = math.isqrt(length)
    if n * n != length:
        return "No"

    for i in range(n):
        for j in range(n):
            sym_i = n - 1 - i
            sym_j = n - 1 - j
            if grid[i * n + j] != grid[sym_i * n + sym_j]:
                return "No"
    return "Yes"
