def unused_digits(*numbers):
    digits = "0123456789"
    for number in list(numbers):
        for d in str(number):
            digits = digits.replace(d, '')
        
    return digits
