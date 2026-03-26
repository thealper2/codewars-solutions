def stalin_sort(arr):
    if not arr:
        return None
    
    i = 1
    prev = arr[0]
    while i < len(arr):
        if arr[i] >= prev:
            prev = arr[i]
            i += 1
        else:
            del arr[i]
        
