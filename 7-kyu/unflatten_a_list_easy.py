def unflatten(flat_array):
    result = []
    i = 0
    n = len(flat_array)

    while i < n:
        current = flat_array[i]
        if current < 3:
            result.append(current)
            i += 1
        else:
            sub_array_length = current
            end = i + sub_array_length
            if end > n:
                end = n
            sub_array = flat_array[i:end]
            result.append(sub_array)
            i = end

    return result
