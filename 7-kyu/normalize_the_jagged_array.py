def normalize(arr, fill_value=None):
    if not arr:
        return []
    
    max_len = max([len(row) for row in arr])
    n = len(arr)
    
    for i in range(n):
        l = max_len - len(arr[i])
        for _ in range(l):
            arr[i].append(fill_value)
            
    return arr
