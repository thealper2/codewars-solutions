def wheat_from_chaff(values):
    result = list(values)
    n = len(result)
    left, right = 0, n - 1
    
    while left < right:
        while left < right and result[left] < 0:
            left += 1
            
        while left < right and result[right] > 0:
            right -= 1
            
        if left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
            
    return result