def mult_implication(arr):
    if not arr:
        return None
    
    n = len(arr)
    result = True
    for item in arr:
        result = not result or item
    
    return result
