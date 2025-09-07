def game(n, m):
    if m == 2:
        return 'second'
    if n % 2 == 0:
        return 'second'
    else:
        return 'first'
