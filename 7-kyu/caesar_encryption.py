def caeser(message, key):
    result = ""
    for c in message:
        if c.isalpha():
            result += chr((ord(c.upper()) - ord('A') + key) % 26 + ord('A'))
        else:
            result += c
            
    return result
