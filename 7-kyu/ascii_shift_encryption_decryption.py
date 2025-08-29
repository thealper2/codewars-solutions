def ascii_encrypt(plaintext):
    ciphertext = []
    for i, char in enumerate(plaintext):
        new_char = chr(ord(char) + i)
        ciphertext.append(new_char)
        
    return ''.join(ciphertext)
    
def ascii_decrypt(encrypted):
    plaintext = []
    for i, char in enumerate(encrypted):
        new_char = chr(ord(char) - i)
        plaintext.append(new_char)
    
    return ''.join(plaintext)
