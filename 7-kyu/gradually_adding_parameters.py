def add(*args):
    args = list(args)
    result = 0
    for i, arg in enumerate(args):
        result += (i + 1) * arg

    return result
