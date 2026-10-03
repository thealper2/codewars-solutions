def find_children(dancing_brigade):
    s = sorted(dancing_brigade)
    freq = {}
    for c in s:
        if c.isupper():
            if c in freq:
                freq[c] = c + freq[c]
            else:
                freq[c] = ''
        else:
            if c.upper() in freq:
                freq[c.upper()] += c
                
    result = ''
    for k, v in freq.items():
        result += k + v
        
    return result