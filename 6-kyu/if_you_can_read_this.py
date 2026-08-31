from preloaded import NATO

def to_nato(words : str) -> str:
    result = []
    for char in words:
        if char.isspace():
            continue
        elif char.isalpha():
            result.append(NATO[char.upper()])
        else:
            result.append(char)
            
    return ' '.join(result)