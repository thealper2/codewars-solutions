def find_longest(arr):
    max_l = float('-inf')
    max_val = float('-inf')
    for num in arr:
        l = len(str(num))
        if l > max_l and num > max_val:
            max_l = l
            max_val = num
            
    return max_val