def gordon(a):
    words = a.split()
    n = len(words)
    
    for i in range(n):
        words[i] = words[i].upper()
        words[i] = words[i].replace('A', '@')
        words[i] = words[i].replace('E', '*')
        words[i] = words[i].replace('I', '*')
        words[i] = words[i].replace('O', '*')
        words[i] = words[i].replace('U', '*')
        words[i] += '!!!!'
        
    return ' '.join(words)