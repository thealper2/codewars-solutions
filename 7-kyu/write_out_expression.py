def expression_out(exp):
    parts = exp.split()
    if len(parts) != 3:
        return "That's not an operator!"
    
    a, op, b = parts
    operators = {
        "+": "Plus",
        "-": "Minus",
        "*": "Times",
        "/": "Divided By",
        "**": "To The Power Of",
        "=": "Equals",
        "!=": "Does Not Equal"
    }
    numbers = {
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten'
    }
    if op not in operators:
        return "That's not an operator!"
    
    if a not in numbers or b not in numbers:
        return "That's not an operator!"
    
    return f'{numbers[a]} {operators[op]} {numbers[b]}'
    
