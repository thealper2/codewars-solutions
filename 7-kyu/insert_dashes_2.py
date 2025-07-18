def insert_dash2(num):
    if num == 0:
        return '0'
    
    num_str = str(num)
    result = []
    prev_char = None
    
    for char in num_str:
        current_digit = int(char)
        if prev_char is not None:
            prev_digit = int(prev_char)
            if current_digit != 0 and prev_digit != 0:
                if current_digit % 2 == 1 and prev_digit % 2 == 1:
                    result.append('-')
                elif current_digit % 2 == 0 and prev_digit % 2 == 0:
                    result.append('*')
                    
        result.append(char)
        prev_char = char
    
    return ''.join(result)