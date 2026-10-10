def count_adjacent_pairs(st): 
    if not st:
        return 0
    
    words = st.lower().split()
    count = 0
    i = 0
    while i < len(words) - 1:
        if words[i] == words[i + 1]:
            count += 1
            while i < len(words) - 1 and words[i] == words[i + 1]:
                i += 1
                
        i += 1
        
    return count