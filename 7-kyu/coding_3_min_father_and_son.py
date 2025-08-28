def sc(s):
    result = ''
    for c in s:
        if c.isupper() and c.lower() in s:
            result += c
        elif c.islower() and c.upper() in s:
            result += c
            
    return result
