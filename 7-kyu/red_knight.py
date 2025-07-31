def red_knight(N, P):
    if N % 2 == 0 and P % 2 == 0:
        return ('White', P * 2)
    elif N % 2 == 0 and P % 2 == 1:
        return ('Black', P * 2)
    elif N % 2 == 1 and P % 2 == 0:
        return ('Black', P * 2)
    else:
        return ('White', P * 2)
