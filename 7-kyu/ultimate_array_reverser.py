def reverse(a):
    reverse_str = ''.join(a)[::-1]
    lengths = [len(item) for item in a]
    i = 0
    result = []
    for item in a:
        l = len(item)
        result.append(reverse_str[i:i+l])
        i += l
        
    return result

