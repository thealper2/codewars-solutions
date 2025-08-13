def solve(s):
    uppercase_letters = 0
    lowercase_letters = 0
    numbers = 0
    special_characters = 0
    
    for c in s:
        if c.isdigit():
            numbers += 1
        elif c.isalpha():
            if c.islower():
                lowercase_letters += 1
            else:
                uppercase_letters += 1
        else:
            special_characters += 1
            
    return [uppercase_letters, lowercase_letters, numbers, special_characters]