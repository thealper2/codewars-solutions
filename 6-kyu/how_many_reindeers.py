def reindeer(presents):
    if presents < 0:
        raise ValueError('Invalid number of presents')

    required = 2 + (presents + 29) // 30
    if required > 8:
        raise ValueError('Too many presents')

    return required