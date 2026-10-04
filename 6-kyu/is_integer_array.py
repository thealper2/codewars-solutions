def is_int_array(arr):
    return isinstance(arr, list) and all(
        isinstance(x, (int, float)) and not isinstance(x, bool) and x % 1 == 0
        for x in arr
    )