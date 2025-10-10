def min_value(arr, n):
    result = []
    for i in range(len(arr) - n + 1):
        sub = arr[i:i+n]
        result.append(min(sub))

    return result
