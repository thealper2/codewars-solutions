def duplicate_sandwich(arr):
    seen = {}
    for i, item in enumerate(arr):
        if item in seen:
            start = seen[item] + 1
            end = i
            return arr[start:end]
        
        seen[item] = i
