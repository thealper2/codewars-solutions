def range_function(*args):
    if len(args) == 1:
        start, step, stop = 1, 1, args[0]
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, step, stop = args
    else:
        raise TypeError('range_function takes 1 to 3 arguments')

    current = start
    while current <= stop:
        yield current
        current += step