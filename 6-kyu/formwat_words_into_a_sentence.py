def format_words(words):
    if not words:
        return ''
    
    words = [word for word in words if word != '']
    if not words:
        return ''
    
    if len(words) == 1:
        return words[0]
    
    return ', '.join(words[:-1]) + " and " + words[-1]