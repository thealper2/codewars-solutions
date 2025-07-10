def array_change(arr):
    total = 0
    n = len(arr)
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            temp = arr[i]
            arr[i] = arr[i - 1] + 1
            total += arr[i] - temp
            
    return total
