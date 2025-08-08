def get_weight(name):
    total = 0
    for c in name:
        if c == ' ' or c.isdigit():
            continue
        elif c.isupper():
            total += ord(c) + 32
        elif c.islower():
            total += ord(c) - 32
            
    return total
