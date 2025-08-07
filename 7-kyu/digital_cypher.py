def encode(message, key):
    n = len(message)
    key_digits = [int(d) for d in str(key)]
    key_length = len(key_digits)
    
    encoded_numbers = []
    for i in range(n):
        digit = ord(message[i]) - 96
        key_digit = key_digits[i % key_length]
        encoded_number = digit + key_digit
        encoded_numbers.append(encoded_number)
        
    
    return encoded_numbers
