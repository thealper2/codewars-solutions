def make_sentences(parts):
    result = ''
    for part in parts:
        if part == ',':
            result += ','
        elif part.startswith('.'):
            break
        else:
            if result:
                result += ' '
            
            result += part
            
    return result + '.'