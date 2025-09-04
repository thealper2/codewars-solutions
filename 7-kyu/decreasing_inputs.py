def add(*args):
    result = 0
    args = list(args)
    for i in range(len(args)):
        result += args[i] / (i + 1)
        
    return round(result)
