def multiply_and_filter(seq, multiplier): 
    result = []
    for item in seq:
        if item is not False and item is not True and (isinstance(item, int) or isinstance(item, float)):
            result.append(item * multiplier)

    return result
