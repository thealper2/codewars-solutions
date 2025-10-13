def index_equals_value(arr):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == mid:
            result = mid
            right = mid - 1
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
