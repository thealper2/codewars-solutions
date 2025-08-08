def is_sorted_and_how(arr):
    asc = sorted(arr)
    desc = sorted(arr, reverse=True)
    
    if arr == asc:
        return 'yes, ascending'
    elif arr == desc:
        return 'yes, descending'
    else:
        return 'no'
    
