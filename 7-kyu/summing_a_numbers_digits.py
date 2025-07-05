def sum_digits(number):
    if number < 0:
        number *= -1
        
    return sum([int(d) for d in str(number)])