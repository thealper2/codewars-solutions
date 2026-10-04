from functools import reduce

def chained(functions):
    func_list = list(functions)
    return lambda x: reduce(lambda acc, f: f(acc), func_list, x)