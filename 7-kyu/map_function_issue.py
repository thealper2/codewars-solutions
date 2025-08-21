def map(arr, func):
    if not callable(func):
        return 'given argument is not a function'
    
    converted_arr = []
    for x in arr:
        if isinstance(x, (int, float)):
            converted_arr.append(x)
        elif isinstance(x, str):
            try:
                num = float(x)
                converted_arr.append(num)
            except ValueError:
                return 'array should contain only numbers'
        else:
            return 'array should contain only numbers'
    
    return [func(x) for x in converted_arr]

def func(x):
    return x % 2 == 0
