def solve(s):
    chars = [c for c in s if c != ' ']
    chars.reverse()
    result = []
    index = 0
    
    for c in s:
        if c == ' ':
            result.append(' ')
        else:
            result.append(chars[index])
            index += 1
    
    return ''.join(result)