def cap_me(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i].capitalize()
        
    return arr