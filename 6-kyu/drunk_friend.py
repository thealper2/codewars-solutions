def decode(string_):
    if not isinstance(string_, str):
        return 'Input is not a string'
    
    result = ''
    for c in string_:
        if c.isupper():
            result += chr(ord('A') + (ord('Z') - ord(c)) % ord('A'))
        elif c.islower():
            result += chr(ord('a') + (ord('z') - ord(c)) % ord('a'))
        else:
            result += c
    
    return result