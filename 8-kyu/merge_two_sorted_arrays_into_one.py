def merge_arrays(arr1, arr2):
    arr = list(set(arr1 + arr2))

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
