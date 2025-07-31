def greet(name):
    if isinstance(name, str):
        if len(name) > 0:
            return "hello " + name + "!"

    return None
