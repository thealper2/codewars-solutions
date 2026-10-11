def group(arr):
    d = {}
    for item in arr:
        if item not in d:
            d[item] = [item]a
        else:
            d[item].append(item)
        
    return [v for v in d.values()]