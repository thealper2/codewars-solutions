def switch_lights(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            for j in range(i + 1):
                arr[j] = 1 - arr[j]
    return arr
