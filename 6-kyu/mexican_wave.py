def wave(people):
    result = []
    for i, c in enumerate(people):
        if c != ' ':
            result.append(people[:i] + c.upper() + people[i + 1:])
            
    return result