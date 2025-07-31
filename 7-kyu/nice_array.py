def is_nice(arr):
    if not arr:
        return False

    arr = set(arr)
    for c in arr:
        if (c - 1 not in arr) and (c + 1 not in arr):
            return False

    return True
