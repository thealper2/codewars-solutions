def re_ordering(text):
    words = text.split()
    result = []
    for word in words:
        if word[0].isupper():
            result.insert(0, word)
        else:
            result.append(word)

    return " ".join(result)
