def passed_pawn(board):
    pr = pc = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == 'P':
                pr, pc = r, c
                break
        if pr is not None:
            break

    for r in range(0, pr):
        for c in (pc - 1, pc, pc + 1):
            if 0 <= c < 8 and board[r][c] == 'p':
                return False

    return True