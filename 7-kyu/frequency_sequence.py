def freq_seq(s, sep):
    freq = {}
    result = []
    for c in s:
        if c not in freq:
            freq[c] = str(s.count(c))
        
        result.append(freq[c])
        
    return sep.join(result)
