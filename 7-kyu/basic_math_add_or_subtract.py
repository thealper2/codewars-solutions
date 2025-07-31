def calculate(s):
    result = 0
    i = 0
    num = 0
    operation = None

    def extract_number(s, i):
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        return int(num_str), i

    result, i = extract_number(s, i)

    while i < len(s):
        if s.startswith("plus", i):
            operation = "plus"
            i += 4
        elif s.startswith("minus", i):
            operation = "minus"
            i += 5
        else:
            pass

        num, i = extract_number(s, i)

        if operation == "plus":
            result += num
        elif operation == "minus":
            result -= num

    return str(result)
