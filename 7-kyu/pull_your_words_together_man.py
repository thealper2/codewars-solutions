def sentencify(words):
    return ' '.join([words[0][0].upper() + words[0][1:]] + words[1:]) + '.'