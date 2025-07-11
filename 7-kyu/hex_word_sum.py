def hex_word_sum(s):
    s = s.replace('O', '0')
    s = s.replace('S', '5')
    words = s.split()
    total = 0
    for word in words:
        valid = True
        for char in word.upper():
            if char not in '0123456789ABCDEF':
                valid = False
                break
                
        if valid and word:
            total += int(word, 16)
    return total
