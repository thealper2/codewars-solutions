def two_sort(array):
    array.sort()
    return "***".join([item[0] for item in array[0]])
