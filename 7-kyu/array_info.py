def array_info(arr):
    if not arr:
        return "Nothing in the array!"
    
    length = len(arr)
    integers = 0
    floats = 0
    strings = 0
    whitespaces = 0
    
    for item in arr:
        if isinstance(item, int):
            integers += 1
        elif isinstance(item, float):
            floats += 1
        elif isinstance(item, str):
            if item.isspace():
                whitespaces += 1
            else:
                strings += 1
                
    result = [
        [length],
        [integers if integers else None],
        [floats if floats else None],
        [strings if strings else None],
        [whitespaces if whitespaces else None]
    ]
    return result
