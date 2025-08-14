def find_next_square(sq):
    d = sq ** 0.5
    if d // 1 == d:
        return (d + 1) ** 2

    return -1
