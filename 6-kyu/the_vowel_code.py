def encode(st):
    d = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    result = ''
    for c in st:
        if c in 'aeiou':
            result += str(d[c])
        else:
            result += c
            
    return result
    
def decode(st):
    d = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    result = ''
    for c in st:
        if c in '12345':
            result += str(d[c])
        else:
            result += c
            
    return result
