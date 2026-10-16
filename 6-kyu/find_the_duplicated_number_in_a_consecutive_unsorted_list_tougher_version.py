def find_dup(arr):
    n = len(arr) - 1
    result = 0
    
    for i in range(1, n + 1):
        result ^= i
    
    for x in arr:
        result ^= x
    
    return result