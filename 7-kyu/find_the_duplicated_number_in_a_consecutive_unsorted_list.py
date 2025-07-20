def find_dup(arr):
    for item in arr:
        if arr.count(item) > 1:
            return item
    
    return 0