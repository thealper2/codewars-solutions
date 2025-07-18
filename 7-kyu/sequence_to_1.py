def seq_to_one(n):
    if n < 1:
        return list(range(n, 2))
    else:
        return list(range(n, 0, -1))
