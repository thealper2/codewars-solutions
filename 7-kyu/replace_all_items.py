def replace_all(obj, find, replace):
    if not obj:
        return []
    
    if type(obj) == str:
        return obj.replace(find, replace)
    
    n = len(obj)
    for i in range(n):
        if obj[i] == find:
            obj[i] = replace
            
    return obj
