def replace_nth(text, n, old_value, new_value):
    if n <= 0:
        return text
    
    count = 0
    result = []
    for char in text:
        if char == old_value:
            count += 1
            if count % n == 0:
                result.append(new_value)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)
