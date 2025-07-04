def cube_odd(arr):
    result = 0
    for num in arr:
        if type(num) not in [int, float]:
            return None
        else:
            if num % 2 == 1:
                result += num ** 3
                
    return result
