def word_to_bin(word):
    return [bin(ord(char))[2:].zfill(8) for char in word]
