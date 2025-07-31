def find_array(arr1, arr2):
    n = len(arr1)
    result = []

    for i in arr2:
        if i <= n - 1:
            result.append(arr1[i])

    return result
