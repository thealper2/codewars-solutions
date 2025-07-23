def initials(name):
    words = name.split()
    n = len(words)
    result = ''
    for i in range(n):
        if i == n - 1:
            result += words[i].capitalize()
        else:
            result += words[i][0].upper() + '.'
            
    return result