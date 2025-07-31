def is_smooth(arr):
    n = len(arr)
    if n == 0:
        return False

    if arr[0] != arr[-1]:
        return False

    if n % 2 == 1:
        middle = arr[n // 2]
    else:
        middle = arr[n // 2 - 1] + arr[n // 2]

    return arr[0] == middle
