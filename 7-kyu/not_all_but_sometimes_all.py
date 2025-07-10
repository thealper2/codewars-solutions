def remove(text, what):
    result = []
    
    for char in text:
        if char in what and what[char] > 0:
            what[char] -= 1
        else:
            result.append(char)
    
    return ''.join(result)
