def min_sum(arr):
    n = (len(arr) + 1) // 2
    min_sum = 0
    for _ in range(n):
        min_ = min(arr)
        max_ = max(arr)
        min_sum += max_ * min_
        arr.remove(min_)
        arr.remove(max_)
        
    return min_sum
