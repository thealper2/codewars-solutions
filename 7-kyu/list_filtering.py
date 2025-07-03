def filter_list(l):
    return list(filter(lambda x: type(x) in [int, float], l))