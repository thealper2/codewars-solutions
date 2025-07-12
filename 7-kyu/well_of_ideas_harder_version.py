def well(arr):
    count = 0
    for a in arr:
        a = list(map(str, a))
        a = list(map(str.lower, a))
        count += a.count('good')
        
    if count == 0:
        return "Fail!"
    elif count <= 2:
        return "Publish!"
    else:
        return "I smell a series!"