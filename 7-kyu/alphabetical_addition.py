def add_letters(*letters):
    if not letters:
        return 'z'
    
    total = sum(ord(c) - ord('a') + 1 for c in letters)
    total %= 26
    if total == 0:
        total = 26
    
    return chr(total + ord('a') - 1)