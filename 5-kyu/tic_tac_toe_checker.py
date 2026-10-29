def win_indexes(n):
    for r in range(n):
        yield [(r, c) for c in range(n)]
    for c in range(n):
        yield [(r, c) for r in range(n)]
    yield [(i, i) for i in range(n)]
    yield [(i, n - 1 - i) for i in range(n)]


def is_solved(board):
    n = len(board)

    for indexes in win_indexes(n):
        if all(board[r][c] == 1 for r, c in indexes):
            return 1
        if all(board[r][c] == 2 for r, c in indexes):
            return 2

    if all(cell != 0 for row in board for cell in row):
        return 0

    return -1