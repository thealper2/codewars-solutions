def calculate(expr: str, values: dict[str, int]) -> int:
    substituted = []
    i = 0
    n = len(expr)
    while i < n:
        if expr[i] in values:
            value = values[expr[i]]
            substituted.append("True" if value else "False")
            i += 1
        else:
            substituted.append(expr[i])
            i += 1
    substituted_expr = "".join(substituted)
    tokens = substituted_expr.replace("&", " & ").replace("|", " | ").split()
    i = 0
    while i < len(tokens) - 2:
        if tokens[i + 1] == "&":
            a = tokens[i] == "True"
            b = tokens[i + 2] == "True"
            result = a and b
            tokens[i : i + 3] = ["True" if result else "False"]
        else:
            i += 1

    i = 0
    while i < len(tokens) - 2:
        if tokens[i + 1] == "|":
            a = tokens[i] == "True"
            b = tokens[i + 2] == "True"
            result = a or b
            tokens[i : i + 3] = ["True" if result else "False"]
        else:
            i += 1

    return tokens[0] == "True"
