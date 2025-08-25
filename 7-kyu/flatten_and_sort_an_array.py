def flatten_and_sort(array):
    result = []
    for sub in array:
        result.extend(sub)
        
    return sorted(result)
