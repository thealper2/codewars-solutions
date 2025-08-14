def last(*args):
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, (list, str)):
            return arg[-1]
        else:
            return arg
    else:
        return args[-1]
