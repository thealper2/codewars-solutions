def is_valid_dni(s: str) -> bool:
    if len(s) != 9:
        return False
    
    numbers = s[:-1]
    letter = s[-1]
    
    if not numbers.isdigit():
        return False
    
    if not letter.isalpha() or not letter.isupper():
        return False
    
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    remainder = int(numbers) % 23
    
    return letters[remainder] == letter.upper()
