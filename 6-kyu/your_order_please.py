def order(sentence):
    words = sentence.split()
    n = len(words)
    result = [''] * n
    for word in words:
        idx = None
        for c in word:
            if c.isdigit():
                idx = int(c)
                break
                
        result[idx - 1] = word
        
    return ' '.join(result)