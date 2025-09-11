def word_splitter(string):
    result = []
    word = ''
    for c in string:
        if not c.isdigit() and not c.isalpha() and c not in ['.', '-']:
            if word:
                result.append(word)
                word = ''
        else:
            word += c
    
    if word:
        result.append(word)
    
    return result
