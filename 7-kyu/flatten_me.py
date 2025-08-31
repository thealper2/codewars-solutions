def flatten_me(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for i in item:
                result.append(i)
                
        else:
            result.append(item)
            
    return result
