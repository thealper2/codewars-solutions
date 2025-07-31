def calculator(txt):
    parts = txt.split()
    a = len(parts[0])
    operator = parts[1]
    b = len(parts[2])

    if operator == "+":
        return "." * (a + b)
    elif operator == "-":
        return "." * (a - b)
    elif operator == "*":
        return "." * (a * b)
    elif operator == "//":
        return "." * (a // b)
    else:
        return "." * (a // b)
