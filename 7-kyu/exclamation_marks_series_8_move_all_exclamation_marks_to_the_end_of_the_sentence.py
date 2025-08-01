def remove(string : str) -> str:
    result = ''
    marks_count = 0
    for c in string:
        if c == '!':
            marks_count += 1
        else:
            result += c
            
    return result + '!' * marks_count
