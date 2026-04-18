def title_case(title, minor_words=''):
    words = title.lower().split()
    minor_words = minor_words.lower().split()
    
    if not minor_words:
        return " ".join(word.capitalize() for word in words)
    
    first_upper = minor_words[0].capitalize()
    n = len(words)
    
    result = []
    for i in range(n):
        word = words[i]
        if i == 0 and word == first_upper:
            result.append(word.capitalize())
        elif i > 0 and word in minor_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    
    return " ".join(result)
