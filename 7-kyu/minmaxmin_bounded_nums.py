def min_min_max(arr):
    min_ = min(arr)
    max_ = max(arr)
    absent = None
    for i in range(min_ + 1, max_):
        if i not in arr:
            absent = i
            break
            
    return [min_, absent, max_]
