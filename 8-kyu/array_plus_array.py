def array_plus_array(arr1, arr2):
    sum = 0
    for x, y in zip(arr1, arr2):
        sum += x + y

    return sum
