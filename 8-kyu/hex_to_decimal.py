def hex_to_dec(inp):
    decimal = 0
    for digit in inp:
        if '0' <= digit <= '9':
            decimal = 16 * decimal + int(digit)
        elif 'A' <= digit <= 'F':
            decimal = 16 * decimal + (ord(digit) - ord('A') + 10)
        elif 'a' <= digit <= 'f':
            decimal = 16 * decimal + (ord(digit) - ord('a') + 10)
        
    return decimal