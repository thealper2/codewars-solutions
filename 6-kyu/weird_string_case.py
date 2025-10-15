def to_weird_case(words):
    result = []
    for word in words.split():
        new_word = ''
        for i, c in enumerate(word):
            if i % 2 == 0:
                new_word += c.upper()
            else:
                new_word += c.lower()
                
        result.append(new_word)
        
    return ' '.join(result)
