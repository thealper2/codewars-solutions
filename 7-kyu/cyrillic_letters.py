def is_cyrillic(letter):
    for char in letter:
        code = ord(char)
        if not (0x0400 <= code <= 0x04FF):
            return False
        
    return True
