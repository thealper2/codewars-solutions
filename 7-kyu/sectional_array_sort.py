def sect_sort(arr, start, num_items=0):
    if num_items <= 0:
        subarray = arr[start:]
        subarray.sort()
        arr[start:] = subarray
    else:
        end = start + num_items
        if end > len(arr):
            end = len(arr)
        subarray = arr[start:end]
        subarray.sort()
        arr[start:end] = subarray
    return arr
