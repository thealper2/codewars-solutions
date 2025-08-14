def determine_winner(board):
    W_count = 0
    B_count = 0
    for row in board:
        W_count += row.count('W')
        B_count += row.count('B')
        
    if W_count > B_count:
        return ('W', W_count)
    elif B_count > W_count:
        return ('B', B_count)
    else:
        return ('T', B_count)
