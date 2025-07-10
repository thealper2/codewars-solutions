def capitals(word):
    n = len(word)
    result = []
    
    for i in range(n):
        if 65 <= ord(word[i]) <= 92:
            result.append(i)
            
    return result
