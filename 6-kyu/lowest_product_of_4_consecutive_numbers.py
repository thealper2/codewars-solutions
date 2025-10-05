def lowest_product(num):
    if len(num) < 4:
        return "Number is too small"
    
    result = float('inf')
    for i in range(0, len(num) - 3):
        digits = list(map(int, num[i:i+4]))
        result = min(result, digits[0] * digits[1] * digits[2] * digits[3])
    
    return result
