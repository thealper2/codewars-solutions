def split_exp(n):
    if n == "0":
        return []

    result = []
    if "." in n:
        integer_part, fractional_part = n.split(".")
    else:
        integer_part = n
        fractional_part = ""

    for i, digit in enumerate(integer_part):
        if digit != "0":
            power = len(integer_part) - i - 1
            num = digit + "0" * power
            result.append(num)

    for j, digit in enumerate(fractional_part):
        if digit != "0":
            num = "." + "0" * j + digit
            result.append(num)

    return sorted(result, key=lambda x: float(x), reverse=True)
