def bubble(arr):
    n = len(arr)
    snapshots = []
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                snapshots.append(arr[:])
                swapped = True
                
    return snapshots
