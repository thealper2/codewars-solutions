def all_non_consecutive(arr):
    n = len(arr)
    result = []
    for i in range(1, n):
        if abs(arr[i] - arr[i - 1]) != 1:
            result.append({'i': i, 'n': arr[i]})
            
    return result
