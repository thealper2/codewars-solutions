def bubblesort_once(l):
    arr = l.copy()
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
