def fix(paragraph):
    if not paragraph:
        return ''
    
    sentences = paragraph.split('. ')
    return '. '.join([sentence[0].upper() + sentence[1:] for sentence in sentences])
