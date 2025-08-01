def decode(code, key):
    key_str = str(key)
    key_digits = [int(d) for d in key_str]
    key_length = len(key_digits)
    
    decoded_numbers = []
    for i in range(len(code)):
        key_digit = key_digits[i % key_length]
        decoded_number = code[i] - key_digit
        decoded_numbers.append(decoded_number)

    decoded_message = []
    for num in decoded_numbers:
        decoded_message.append(chr(num + 96))
    
    return ''.join(decoded_message)
