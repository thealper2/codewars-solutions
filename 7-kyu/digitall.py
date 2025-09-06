def digit_all(x):
    if isinstance(x, str):
        return ''.join([c for c in x if c.isdigit()])
    else:
        return 'Invalid input !'
