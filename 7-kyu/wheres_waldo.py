def find_waldo(crowd):
    all_chars = [char for row in crowd for char in row]
    
    freq = {}
    for char in all_chars:
        freq[char] = freq.get(char, 0) + 1
    
    waldo_char = None
    for char, count in freq.items():
        if count == 1:
            waldo_char = char
            break
    
    if waldo_char is None:
        raise ValueError("Waldo not found in the crowd")
    
    for y in range(len(crowd)):
        row = crowd[y]
        for x in range(len(row)):
            if row[x] == waldo_char:
                return [y, x]
    
    raise ValueError("Waldo not found in the crowd")
