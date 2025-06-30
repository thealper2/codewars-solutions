def _all(seq, fun):
    for s in seq:
        if not fun(s):
            return False

    return True
