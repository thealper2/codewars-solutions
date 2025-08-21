def odd_ones_out(numbers):
    result = []
    for number in numbers:
        if numbers.count(number) % 2 == 0:
            result.append(number)
            
    return result
