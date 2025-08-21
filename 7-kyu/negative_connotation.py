def connotation(strng):
    pos_words = 0
    neg_words = 0
    for word in strng.lower().split():
        if word[0].isalpha():
            if ord('a') <= ord(word[0]) <= ord('m'):
                pos_words += 1
            else:
                neg_words += 1
                
    if pos_words >= neg_words:
        return True
    else:
        return False
