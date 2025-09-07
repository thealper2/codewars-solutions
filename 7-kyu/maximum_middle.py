def maximum_median(arr, min_length):
    n = len(arr)
    l = min_length // 2
    r = n - (min_length - min_length // 2)
    return max(arr[l:r+1])
