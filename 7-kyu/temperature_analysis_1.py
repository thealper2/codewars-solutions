def lowest_temp(t):
    if not t:
        return None

    return min(map(int, t.split(" ")))
