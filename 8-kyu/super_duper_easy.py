def problem(a):
    if type(a).__name__ not in ["float", "int"]:
        return "Error"
    
    return a * 50 + 6
