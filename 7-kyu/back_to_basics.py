def types(x):
    if isinstance(x, bool):
        return "bool"
    elif isinstance(x, int):
        return "int"
    elif isinstance(x, float):
        return "float"
    elif isinstance(x, str):
        return "str"
