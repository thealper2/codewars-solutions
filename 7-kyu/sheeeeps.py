def reload_sheeps(arr):
    result = []
    for i in arr:
        if i.count('e') == 2 and i.count('s') == 1 and i.count('h') == 1 and i.count('p') == 1:
            result.append('sheep')
            
    return result
