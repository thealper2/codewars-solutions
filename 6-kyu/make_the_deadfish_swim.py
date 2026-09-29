def parse(data):
    value = 0
    result = []
    
    for cmd in data:
        if cmd == 'i':
            value += 1
        elif cmd == 'd':
            value -= 1
        elif cmd == 's':
            value *= value
        elif cmd == 'o':
            result.append(value)
            
    return result