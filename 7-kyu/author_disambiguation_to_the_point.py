def could_be(original, another):
    if not original or not another or original.isspace() or another.isspace():
        return False
    
    original_words = original.split()
    another_words = another.split()
    for word in another_words:
        if word not in original_words:
            return False
        
    return True
