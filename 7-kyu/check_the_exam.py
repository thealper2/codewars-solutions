def check_exam(arr1,arr2):
    result = 0
    for a, b in zip(arr1, arr2):
        if b == '': continue
        result = result + 4 if a == b else result - 1
        
    return max(0, result)