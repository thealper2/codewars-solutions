def ones_complement(binary_number):
    result = ''
    for num in binary_number:
        if num == '1':
            result += '0'
        else:
            result += '1'
            
    return result
