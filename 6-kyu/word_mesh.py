def word_mesh(words):
    result = []
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        best = ''
        max_len = min(len(a), len(b))
        for length in range(1, max_len + 1):
            if a[-length:] == b[:length]:
                best = a[-length:]
                
        if not best:
            return "failed to mesh"
        
        result.append(best)
        
    return ''.join(result)