def spacey(array):
    n = len(array)
    for i in range(1, n):
        array[i] = array[i - 1] + array[i]
        
    return array
