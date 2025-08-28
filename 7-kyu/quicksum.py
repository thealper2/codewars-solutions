def quicksum(packet):
    if not all(c == ' ' or ('A' <= c <= 'Z') for c in packet):
        return 0
    
    total = 0
    for i, char in enumerate(packet, start=1):
        if char == ' ':
            continue
        
        value = ord(char) - ord('A') + 1
        total += i * value
    
    return total
