def remove(s):
    words = s.split()
    n = len(words)
    result = []
    
    for i in range(n):
        if words[i].count('!') != 1:
            result.append(words[i])
            
    return ' '.join(result)