def merry_christmas(funcs):
    char_to_func = {}
    for func in funcs:
        char = func()
        char_to_func[char] = func.__name__
    
    target = "Merry Christmas!"
    result = []
    for char in target:
        func_name = char_to_func[char]
        result.append(func_name)
    
    return ','.join(result)
