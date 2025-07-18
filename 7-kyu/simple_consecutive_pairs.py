def pairs(arr):
    n = len(arr)
    count = 0
    for i in range(0, n - 1, 2):
        if abs(arr[i] - arr[i + 1]) == 1:
            count += 1
            
    return count
