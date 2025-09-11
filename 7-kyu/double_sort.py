def db_sort(arr): 
    strs = []
    others = []
    for item in arr:
        if isinstance(item, str):
            strs.append(item)
        else:
            others.append(item)
            
    strs.sort()
    others.sort()
    return others + strs
