def purify(s: str) -> str:
    words = s.split()
    result_words = []
    for word in words:
        n = len(word)
        new_word = []
        for i in range(n):
            if word[i].lower() == 'i':
                continue
                
            if (i > 0 and word[i-1].lower() == 'i') or (i < n-1 and word[i+1].lower() == 'i'):
                continue
            
            new_word.append(word[i])
        purified_word = ''.join(new_word)
        if purified_word:
            result_words.append(purified_word)
    
    return ' '.join(result_words)
