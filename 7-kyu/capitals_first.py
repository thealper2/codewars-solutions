def capitals_first(text):
    uppers = []
    lowers = []
    words = text.split()
    for word in words:
        if word[0].isalpha():
            if word[0].isupper():
                uppers.append(word)
            else:
                lowers.append(word)
            
    return ' '.join(uppers + lowers)
