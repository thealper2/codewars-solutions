def mirror(text):
    words = text.split()
    max_l = max([len(word) for word in words])
    result = ['*' * (max_l + 4)]
    n = len(words)
    for i in range(n):
        padding = max_l - len(words[i])
        result.append('* ' + words[i][::-1] + ' ' * padding + ' *')
        
    result.append('*' * (max_l + 4))
    return '\n'.join(result)
