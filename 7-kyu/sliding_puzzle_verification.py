def is_solved(board):
    N = len(board)
    flattened = [tile for row in board for tile in row]
    return flattened == list(range(N * N))
