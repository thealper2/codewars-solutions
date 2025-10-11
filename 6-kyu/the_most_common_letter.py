def replace_common(st, letter):
    freq = {}
    indexes = {}
    s = ''.join(st.split())
    n = len(s)
    max_val = float('-inf')
    max_char = ''
    max_index = float('-inf')
    
    for i in range(n):
        if s[i] not in freq:
            freq[s[i]] = 1
            indexes[s[i]] = i    
        else:
            freq[s[i]] += 1
            
    for k, v in freq.items():
        if v > max_val or (v == max_val and indexes[k] < max_index):
            max_val = v
            max_char = k
            max_index = indexes[k]
            
    result = st.replace(max_char, letter)
    return result
