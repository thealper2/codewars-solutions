def calculator(x, y, op):
    if type(x).__name__ == "int" and type(y).__name__ == "int":
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"