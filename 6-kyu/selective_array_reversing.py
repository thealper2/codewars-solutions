def sel_reverse(arr, l):
    if l == 0:
        return arr
    
    n = len(arr)
    l = min(n, l)
    result = []
    
    for i in range(0, n, l):
        result.extend(arr[i:i+l][::-1])
        
    return result