def to_camel_case(text):
    if not text:
        return text
    
    words = []
    word = ''
    for c in text:
        if c == '-' or c == '_':
            words.append(word)
            word = ''
        else:
            word += c

    if word:
        words.append(word)
        
    return words[0] + ''.join([word[0].upper() + word[1:] for word in words[1:]])
