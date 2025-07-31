def is_infinite_process(a, b):
    if a > b:
        return True

    return (b - a) % 2 != 0
