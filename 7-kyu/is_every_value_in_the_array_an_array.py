def arr_check(arr):
    if not isinstance(arr, list):
        return False
    for element in arr:
        if not isinstance(element, list):
            return False

    return True
