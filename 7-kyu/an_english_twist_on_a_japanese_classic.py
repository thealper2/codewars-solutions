def game(words):
    if not words:
        return []
    
    result = []
    n = len(words)
    for i in range(n):
        if words[i] == '':
            break
            
        if i == 0:
            result.append(words[i])
            
        else:
            prev = words[i - 1]
            if prev[-1] == words[i][0]:
                result.append(words[i])
            else:
                break
                
    return result
