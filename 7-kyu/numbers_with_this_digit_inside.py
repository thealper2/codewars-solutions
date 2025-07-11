def numbers_with_digit_inside(x, d):
    d = str(d)
    matching_numbers = [num for num in range(1, x + 1) if d in str(num)]
    
    if not matching_numbers:
        return [0, 0, 0]
    
    count = len(matching_numbers)
    total_sum = sum(matching_numbers)
    product = 1
    for num in matching_numbers:
        product *= num
    
    return [count, total_sum, product]
