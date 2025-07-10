def array_previous_less(arr):
    n = len(arr)
    result = [-1] * n
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                result[i] = arr[j]
                break
                
    return result
