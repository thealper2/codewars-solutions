def is_john_lying(a,b,s):
    distance = abs(a) + abs(b)
    if s < distance:
        return False
    
    return (s - distance) % 2 == 0
