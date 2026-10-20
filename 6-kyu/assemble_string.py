def assemble(arr):
    if not arr:
        return ''
    
    length = len(arr[0])
    result = []
    
    for i in range(length):
        chars = {s[i] for s in arr if s[i] != '*'}
        if len(chars) == 1:
            result.append(chars.pop())
        else:
            result.append('#')
            
    return ''.join(result)