def adjacent_double_double_letters(word):
    n = len(word)
    for i in range(n - 3):
        if word[i] == word[i+1] and word[i+2] == word[i+3]:
            return True
        
    return False
