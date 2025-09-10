def median(array):
    n = len(array)
    array.sort()
    mid = n // 2
    if n % 2 == 0:
        return (array[mid] + array[mid - 1]) / 2
    else:
        return array[mid]
