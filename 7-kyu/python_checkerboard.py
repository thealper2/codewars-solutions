def make_checkered_board(n):
    return [['X' if (i+j) % 2 == 0 else 'O' for j in range(n)] for i in range(n)]
