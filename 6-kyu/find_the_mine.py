def mine_location(field):
    n = len(field)
    for i in range(n):
        for j in range(n):
            if field[i][j] == 1:
                return [i, j]