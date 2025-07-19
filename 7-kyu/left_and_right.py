def left(string, i=1):
    if isinstance(i, str):
        i = string.index(i)
        
    return string[:i] if i else ''

def right(string, i=1):
    if isinstance(i, str):
        i = string[::-1].index(i[::-1])
    
    return string[-i:] if i else ''