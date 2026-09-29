def encrypt(text, n):
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[::2]
    
    return text


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    
    length = len(encrypted_text)
    odd_count = length // 2
    for _ in range(n):
        odd = encrypted_text[:odd_count]
        even = encrypted_text[odd_count:]
        chars = [''] * length
        chars[::2] = even
        chars[1::2] = odd
        encrypted_text = ''.join(chars)
        
    return encrypted_text