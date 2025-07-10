def is_thue_morse(seq):
    if not seq:
        return True
    
    thue_morse = [0]
    while len(thue_morse) < len(seq):
        complement = [1 - bit for bit in thue_morse]
        thue_morse += complement
    
    return seq == thue_morse[:len(seq)]
