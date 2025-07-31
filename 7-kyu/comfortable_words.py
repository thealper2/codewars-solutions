def comfortable_word(word):
    left = 'qwertasdfgzxcvb'
    right = 'yuiouphjklnm'
    if word[0] in left:
        l = True
    else:
        l = False
        
    for c in word:
        if l and c not in left:
            return False
        elif not l and c not in right:
            return False
        
        l = not l
        
    return True
