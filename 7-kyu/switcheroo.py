def switcheroo(s):
    result = ''
    for c in s:
        if c == 'c':
            result += c
        elif c == 'a':
            result += 'b'
        elif c == 'b':
            result += 'a'
            
    return result
