def crazy_formula(number):
    while number >= 10:
        digits = [int(d) for d in str(number)]
        num_digits = len(digits)
        
        if num_digits % 2 == 0:
            digits = digits[:-1]
            num_digits -= 1
        
        if num_digits == 1:
            number = digits[0]
            continue
        
        middle_index = num_digits // 2
        middle_digit = digits[middle_index]
        last_digit = digits[-1]
        
        if middle_digit % 2 != 0:
            digits[middle_index] = -middle_digit
        elif middle_digit % 2 == 0 and last_digit % 2 == 0:
            digits[-1] = -last_digit
        elif middle_digit % 2 == 0 and last_digit % 2 != 0:
            digits[0] = digits[0] ** 2
        
        number = sum(digits)
        if number < 0:
            number = abs(number)
    
    return number