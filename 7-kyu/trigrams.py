def trigrams(phrase):
    phrase = phrase.replace(' ', '_')
    n = len(phrase)
    result = []
    for i in range(n - 2):
        result.append(phrase[i:i+3])
        
    return ' '.join(result)
