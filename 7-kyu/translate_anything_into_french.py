def i_speak_french(sentence):
    result = []
    words = sentence.split()
    n = len(words)
    for i in range(n):
        if i == 0 or (i > 0 and words[i - 1].endswith('.')):
            result.append('Baguette')
        else:
            result.append('baguette')
            
        if i == n - 1 or (i < n - 1 and words[i].endswith('.')):
            result.append('Encore!')
            
    return ' '.join(result)
