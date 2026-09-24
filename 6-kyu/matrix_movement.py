def move(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    r = c = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                r, c = i, j

    def step(command):
        nonlocal r, c
        if command == 'up':
            r = (r - 1) % rows
        elif command == 'down':
            r = (r + 1) % rows
        elif command == 'left':
            c = (c - 1) % cols
        elif command == 'right':
            c = (c + 1) % cols
        elif command == 'stop':
            result = [[0] * cols for _ in range(rows)]
            result[r][c] = 1
            return result

        return step

    return step