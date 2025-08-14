def digit_multiplication(s):
    segments = []
    current_segment = []
    for char in s:
        if char.isdigit():
            current_segment.append(char)
        else:
            if current_segment:
                segments.append(''.join(current_segment))
                current_segment = []
            segments.append(char)
    if current_segment:
        segments.append(''.join(current_segment))
    
    products = []
    operators = []
    for segment in segments:
        if segment.isdigit():
            product = 1
            for digit in segment:
                product *= int(digit)
            products.append(product)
        else:
            operators.append(segment)
    
    if not products:
        return 0
    
    result = products[0]
    for i in range(len(operators)):
        operator = operators[i]
        next_product = products[i + 1]
        if operator == '+':
            result += next_product
        elif operator == '-':
            result -= next_product
    return result
