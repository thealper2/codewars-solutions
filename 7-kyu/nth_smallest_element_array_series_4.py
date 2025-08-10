def nth_smallest(arr, pos):
    min_val = float('inf')
    while pos:
        min_val = min(arr)
        arr.remove(min_val)
        pos -= 1
        
    return min_val