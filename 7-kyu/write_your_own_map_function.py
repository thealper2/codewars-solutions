def map(function, iterable):
    result = []
    for item in iterable:
        result.append(function(item))
        
    return result
