import math


def check_root(string):
    try:
        arr = [int(x.strip()) for x in string.split(',')]
        if len(arr) != 4:
            return "incorrect input"
        
        if any(arr[i] + 1 != arr[i + 1] for i in range(len(arr) - 1)):
            return "not consecutive"
        
        product = 1
        for num in arr:
            product *= num
            
        target = product + 1
        root = math.isqrt(target)
        return f"{target}, {root}"
    
    except (ValueError, AttributeError):
        return "incorrect input"
