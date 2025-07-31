def sum_arrays(arrays, shift):
    result = arrays[0].copy()
    current_length = len(result)
    n = len(arrays)
    
    for i in range(1, n):
        current_shift = i * shift
        array = arrays[i]
        for j in range(len(array)):
            pos = current_shift + j
            if pos < current_length:
                result[pos] += array[j]
            else:
                result.append(array[j])
        current_length = len(result)
    
    return result
