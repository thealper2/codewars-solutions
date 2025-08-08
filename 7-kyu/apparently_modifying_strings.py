def apparently(st):
    words = st.split()
    n = len(words)
    
    for i in range(n):
        if words[i] == 'but' or words[i] == 'and':
            if i < n - 1 and words[i + 1] != 'apparently':
                words[i] = words[i] + ' apparently'
            elif i == n - 1:
                words[i] = words[i] + ' apparently'
                
    return ' '.join(words)
