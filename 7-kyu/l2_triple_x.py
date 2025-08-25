def triple_x(s):
    index = s.find('x')
    if index == -1:
        return False
    
    return s[index:index+3] == 'xxx'
