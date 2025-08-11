def averages(arr):
    if not arr or len(arr) < 2:
        return []
    
    return [(arr[i] + arr[i + 1]) / 2 for i in range(len(arr) - 1)]