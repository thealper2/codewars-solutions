def letters_to_numbers(s):
    result = 0.0
    for c in s:
        ord_c = ord(c)
        if c.isdigit():
            result += int(c)
        elif 65 <= ord_c <= 90:
            result += 2 * (ord_c - 64)
        elif 97 <= ord_c <= 122:
            result += ord_c - 96
            
    return result