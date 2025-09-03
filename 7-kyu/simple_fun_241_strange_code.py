def strange_code(s, e):
    result = []
    last = None
    while s < e - 1:
        s += 1
        e -= 1
        if last is None:
            result.append('a')
            last = 'a'
        else:
            if last == 'a':
                result.append('b')
                last = 'b'
            else:
                result.append('a')
                last = 'a'
                
    return ''.join(result)
