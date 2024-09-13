def sum_of_differences(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    c = 0
    for i in range(len(arr) - 1):
        c += arr[i] - arr[i+1]
    
    return c