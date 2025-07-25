def validate_ean(code):
    total = 0
    for i in range(12):
        digit = int(code[i])
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3
    
    check_digit = (10 - (total % 10)) % 10
    return int(code[-1]) == check_digit