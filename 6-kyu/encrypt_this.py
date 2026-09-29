def encrypt_this(text):
    result = []
    for word in text.split():
        p1 = str(ord(word[0]))
        if len(word) == 1:
            result.append(p1)
            continue
            
        p2 = word[-1]
        if len(word) == 2:
            result.append(p1 + p2)
            continue
            
        p3 = word[2:-1] + word[1]
        result.append(p1 + p2 + p3)

    return ' '.join(result)