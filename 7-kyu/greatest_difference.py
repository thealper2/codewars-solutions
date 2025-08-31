def diff(arr):
    if not arr:
        return False
    
    max_diff = float('-inf')
    max_item = None
    
    for item in arr:
        numbers = item.split('-')
        diff = abs(int(numbers[1]) - int(numbers[0]))
        if diff > max_diff:
            max_diff = diff
            max_item = item
            
    if max_diff == 0:
        return False
            
    return max_item
