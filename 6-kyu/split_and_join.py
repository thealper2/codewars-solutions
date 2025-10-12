def split(arr):
    result = []
    for a in arr:
        result.extend(a)
        
    len_arr = [[len(a)] for a in arr]
    return result, len_arr

def join(arr1, arr2):
    result = []
    idx = 0
    for l in arr2:
        result.append(arr1[idx:idx+l[0]])
        idx += l[0]
        
    return result
