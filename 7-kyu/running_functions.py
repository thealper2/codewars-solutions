def running(lst, fn):
    result = []
    current = None
    for i, val in enumerate(lst):
        if i == 0:
            current = val
        else:
            current = fn(current, val)
        result.append(current)
    return result
