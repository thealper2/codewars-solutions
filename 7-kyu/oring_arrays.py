def or_arrays(arr1, arr2, default=0):
    max_len = max(len(arr1), len(arr2))
    result = []
    for i in range(max_len):
        val1 = arr1[i] if i < len(arr1) else default
        val2 = arr2[i] if i < len(arr2) else default
        result.append(val1 | val2)
        
    return result
