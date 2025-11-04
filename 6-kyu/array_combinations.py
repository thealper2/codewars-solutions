def solve(arr):
    result = 1
    for sub in arr:
        result *= len(set(sub))
        
    return result
