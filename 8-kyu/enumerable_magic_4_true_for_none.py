def none(lst, func):
    return all(not func(item) for item in lst)
