def check_concatenated_sum(number, n):
    if n == 0:
        return False
    
    original_number = number
    is_negative = number < 0
    number = abs(number)
    
    digits = [int(d) for d in str(number)]
    concatenated_numbers = []
    
    for digit in digits:
        concatenated = int(str(digit) * n)
        concatenated_numbers.append(concatenated)
    
    total = sum(concatenated_numbers)
    if is_negative:
        total = -total
    
    return total == original_number
