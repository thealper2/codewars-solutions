def find_odd_names(lst): 
    result = []
    for i in lst:
        name = i['firstName']
        total = sum(ord(c) for c in name)
        if total % 2 == 1:
            result.append(i)
    
    return result