def compress(sentence):
    seen = {}
    words = list(map(str.lower, sentence.split()))
    result = ''
    i = 0
    for word in words:
        if word not in seen:
            seen[word] = i
            i += 1
            result += str(seen[word])
        else:
            result += str(seen[word])
            
    return result
