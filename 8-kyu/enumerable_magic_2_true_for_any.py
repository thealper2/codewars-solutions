def any_(lst, func):
    return any(func(item) for item in lst)
