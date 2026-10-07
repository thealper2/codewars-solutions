def numericals(s):
    freq = {}
    result = ''
    for c in s:
        freq[c] = freq.get(c, 0) + 1
        result += str(freq[c])
        
    return result