def first_reverse_try(arr):
    if len(arr) <= 1:
        return arr
    
    return [arr[-1]] + arr[1:-1] + [arr[0]]
