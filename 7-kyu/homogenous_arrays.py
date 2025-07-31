def filter_homogenous(arrays):
    result = []
    for array in arrays:
        if len(array) == 0:
            continue

        first_type = type(array[0])
        homogenous = True
        for element in array[1:]:
            if type(element) != first_type:
                homogenous = False
                break

        if homogenous:
            result.append(array)

    return result
