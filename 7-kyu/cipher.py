def encode(text: str):
    return ''.join(chr(ord(c) * 6) for c in text)

    
def decode(cipher: str):
    return ''.join(chr(ord(c) // 6) for c in cipher)
    
    
