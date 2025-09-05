def create_dict(keys, values):
    d = {}
    for i, key in enumerate(keys):
        if i < len(values):
            d[key] = values[i]
        else:
            d[key] = None
            
    return d
