def array_manip(array):
    n = len(array)
    for i in range(n):
        right_elements = array[i + 1 :]
        candidates = [x for x in right_elements if x > array[i]]
        if candidates:
            array[i] = min(candidates)
        else:
            array[i] = -1
    return array
