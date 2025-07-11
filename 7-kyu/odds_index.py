def odd_ball(arr):
    odd_index = None
    for i, element in enumerate(arr):
        if isinstance(element, str):
            if len(element) % 2 != 0:
                odd_index = i
                break
    if odd_index is not None:
        for element in arr:
            if isinstance(element, int) and element == odd_index:
                return True
    return False
