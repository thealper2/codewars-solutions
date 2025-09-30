def args_to_string(args):
    result = []
    for arg in args:
        if isinstance(arg, list):
            if len(arg) == 1:
                result.append(arg[0])
            else:
                prefix = '-' if len(arg[0]) == 1 else '--'
                result.append(prefix + arg[0])
                result.append(arg[1])
        else:
            result.append(arg)
            
    return ' '.join(result)
