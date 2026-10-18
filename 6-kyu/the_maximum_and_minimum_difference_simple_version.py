def max_and_min(arr1,arr2):
    max_diff = max(abs(max(arr1) - min(arr2)), abs(max(arr2) - min(arr1)))
    
    a = sorted(arr1)
    b = sorted(arr2)
    i = j = 0
    min_diff = float('inf')
    
    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        if diff < min_diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
            
    return [max_diff, min_diff]