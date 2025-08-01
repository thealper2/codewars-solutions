def testit(s):
    words = s.split()
    transformed_words = []
    for word in words:
        if not word:
            continue
        
        lower_word = word.lower()
        if len(lower_word) == 0:
            transformed_word = ''
        else:
            transformed_word = lower_word[:-1] + lower_word[-1].upper()
        
        transformed_words.append(transformed_word)
        
    return ' '.join(transformed_words)
