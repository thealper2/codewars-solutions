def get_real_floor(n):
    if n > 0:
        if n >= 13:
            return n - 2
        else:
            return n - 1

    else:
        return n
