def array_center(arr):
    if not arr:
        return []
    
    min_a = min(arr)
    avg_a = sum(arr) / len(arr)
    b = [x for x in arr if abs(x - avg_a) < min_a]
    return b