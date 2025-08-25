def sum_even_numbers(seq): 
    result = 0
    for num in seq:
        if num % 2 == 0:
            result += num
            
    return result
