def combine(*args):
    objects = list(args)
    result = {}
    for object in objects:
        for k, v in object.items():
            if k not in result:
                result[k] = v
            else:
                result[k] += v
                
    return result