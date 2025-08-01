def drop_while(arr, pred):
    for i, item in enumerate(arr):
        if not pred(item):
            return arr[i:]
        
    return []
