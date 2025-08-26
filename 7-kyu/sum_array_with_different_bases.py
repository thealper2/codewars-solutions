def sum_it_up(numbers_with_bases):
    result = 0
    for number_with_base in numbers_with_bases:
        n, b = number_with_base
        result += int(n, b)
        
    return result
