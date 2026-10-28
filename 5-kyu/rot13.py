def rot13(message):
    result = ''
    for c in message:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += c
            
    return result