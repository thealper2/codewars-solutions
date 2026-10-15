import re


def calculate_string(string):
    match = re.search(r'([+\-*/])', string)
    op = match.group(1)
    op_pos = match.start()

    left_part = string[:op_pos]
    right_part = string[op_pos + 1:]

    def extract_number(part):
        cleaned = re.sub(r'[^0-9.]', '', part)
        return float(cleaned)

    a = extract_number(left_part)
    b = extract_number(right_part)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    else:
        result = a / b

    return str(round(result))