def sort_array(source_array):
    odd_index = [i for i, n in enumerate(source_array) if n % 2 == 1]
    odd_values = sorted(source_array[i] for i in odd_index)
    result = source_array.copy()
    for idx, n in zip(odd_index, odd_values):
        result[idx] = n
        
    return result