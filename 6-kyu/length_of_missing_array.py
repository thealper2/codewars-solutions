def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0
    
    if any(arr is None or len(arr) == 0 for arr in array_of_arrays):
        return 0

    lengths = sorted(len(arr) for arr in array_of_arrays)
    n = len(lengths)
    expected_start = lengths[0]

    for i in range(n):
        if lengths[i] != expected_start + i:
            return expected_start + i

    return expected_start + n