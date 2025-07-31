def calc_type(a, b, res) -> str:
    if a - b == res:
        return "subtraction"
    elif a + b == res:
        return "addition"
    elif a * b == res:
        return "multiplication"
    else:
        return "division"
