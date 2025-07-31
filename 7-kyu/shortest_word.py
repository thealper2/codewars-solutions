def find_short(s):
    min_len = float("inf")
    for w in s.split():
        if len(w) < min_len:
            min_len = len(w)

    return min_len
