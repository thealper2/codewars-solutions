def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    
    if len(array1) != len(array2):
        return False
    
    a = sorted(x * x for x in array1)
    b = sorted(array2)
    return a == b