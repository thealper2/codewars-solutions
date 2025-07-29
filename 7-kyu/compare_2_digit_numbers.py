def compare(a, b):
    a_digits = [a // 10, a % 10]
    b_digits = [b // 10, b % 10]

    matches = 0
    if a_digits[0] in b_digits:
        matches += 1
    
    if a_digits[1] in b_digits and (a_digits[0] != a_digits[1] or b_digits.count(a_digits[1]) >= 2):
        matches += 1
    
    similarity = matches * 50
    return f"{similarity}%"