def encode(message):
    substitution = {
        'g': 'a', 'G': 'A',
        'a': 'g', 'A': 'G',
        'd': 'e', 'D': 'E',
        'e': 'd', 'E': 'D',
        'r': 'y', 'R': 'Y',
        'y': 'r', 'Y': 'R',
        'p': 'o', 'P': 'O',
        'o': 'p', 'O': 'P',
        'l': 'u', 'L': 'U',
        'u': 'l', 'U': 'L',
        'k': 'i', 'K': 'I',
        'i': 'k', 'I': 'K'
    }
    
    result = ""
    for c in message:
        result += substitution.get(c, c)
    
    return result
    
def decode(message):
    substitution = {
        'g': 'a', 'G': 'A',
        'a': 'g', 'A': 'G',
        'd': 'e', 'D': 'E',
        'e': 'd', 'E': 'D',
        'r': 'y', 'R': 'Y',
        'y': 'r', 'Y': 'R',
        'p': 'o', 'P': 'O',
        'o': 'p', 'O': 'P',
        'l': 'u', 'L': 'U',
        'u': 'l', 'U': 'L',
        'k': 'i', 'K': 'I',
        'i': 'k', 'I': 'K'
    }
    
    result = ""
    for c in message:
        result += substitution.get(c, c)
    
    return result
