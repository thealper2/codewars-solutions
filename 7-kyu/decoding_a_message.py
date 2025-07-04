def decode(message):
    mapping = {}
    for i in range(26):
        original_char = chr(ord('a') + i)
        reversed_char = chr(ord('z') - i)
        mapping[original_char] = reversed_char
    
    decoded_message = []
    for char in message:
        if char in mapping:
            decoded_message.append(mapping[char])
        else:
            decoded_message.append(char)
    
    return ''.join(decoded_message)
