def vert_mirror(strng):
    words = strng.split('\n')
    result = []
    for word in words:
        result.append(word[::-1])
        
    return '\n'.join(result)
    
def hor_mirror(strng):
    words = strng.split('\n')
    result = []
    for word in words:
        result.insert(0, word)
        
    return '\n'.join(result)
    
def oper(fct, s):
    return fct(s)