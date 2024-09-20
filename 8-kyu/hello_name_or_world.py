def hello(name=""):
    return f"Hello, {name[0].upper() + name[1:].lower()}!" if name else "Hello, World!"