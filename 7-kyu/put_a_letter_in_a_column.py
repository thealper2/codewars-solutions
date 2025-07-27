def build_row_text(index, character):
    result = ''
    for i in range(10):
        result += '|'
        if i == index:
            result += character
        else:
            result += ' '
        
        if i - 1 == 9:
            result += '|'
            
    return result[:-1]