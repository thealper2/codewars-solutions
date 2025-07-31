def is_all_possibilities(arr):
    n = len(arr)
    if n == 0:
        return False

    arr.sort()
    for i in range(n):
        if arr[i] != i:
            return False

    return True
