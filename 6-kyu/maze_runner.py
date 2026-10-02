def maze_runner(maze, directions):
    n = len(maze)
    start = None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = (i, j)
                break
        if start:
            break

    r, c = start
    for d in directions:
        if d == 'N':
            r -= 1
        elif d == 'S':
            r += 1
        elif d == 'E':
            c += 1
        elif d == 'W':
            c -= 1

        if r < 0 or r >= n or c < 0 or c >= n:
            return "Dead"
        cell = maze[r][c]
        if cell == 1:
            return "Dead"
        if cell == 3:
            return "Finish"

    return "Lost"