def consecutive(arr, a, b):
    n = len(arr)
    for i in range(1, n):
        if arr[i] == a and arr[i - 1] == b:
            return True
        
        if arr[i] == b and arr[i - 1] == a:
            return True
        
    return False
