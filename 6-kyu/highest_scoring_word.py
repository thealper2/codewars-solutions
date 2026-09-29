def high(x):
    words = x.split()
    best_word = None
    best_score = float('-inf')
    
    for word in words:
        score = sum(ord(c) - ord('a') + 1 for c in word)
        if score > best_score:
            best_word = word
            best_score = score
            
    return best_word