def mispelled(word1,word2):
    if abs(len(word1) - len(word2)) > 1:
        return False
    
    if word1 == word2:
        return True
    
    i = 0
    j = 0
    diff = 0
    while i < len(word1) and j < len(word2):
        if word1[i] != word2[j]:
            diff += 1
            if diff > 1:
                return False
            
            if len(word1) > len(word2):
                i += 1
            elif len(word2) > len(word1):
                j += 1
            else:
                i += 1
                j += 1
            
        else:
            i += 1
            j += 1
            
    return True
