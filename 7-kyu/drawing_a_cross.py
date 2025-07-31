def draw_a_cross(n):
    if n < 3:
        return "Not possible to draw cross for grids less than 3x3!"
    if n % 2 == 0:
        return "Centered cross not possible!"

    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or i + j == n - 1:
                row.append("x")
            else:
                row.append(" ")
        grid.append("".join(row))
    return "\n".join(grid)
