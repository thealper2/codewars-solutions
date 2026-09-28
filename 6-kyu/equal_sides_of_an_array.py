def find_even_index(arr):
    total = sum(arr)
    left = 0
    for i, x in enumerate(arr):
        if left == total - left - x:
            return i
        
        left += x
        
    return -1