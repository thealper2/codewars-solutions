def binary_array_to_number(arr):
    val = 0
    p = len(arr) - 1
    for num in arr:
        val += num * (2 ** p)
        p -= 1
        
    return val