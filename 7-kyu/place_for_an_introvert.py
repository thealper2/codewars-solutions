def introverted_seat(seats: str) -> str | None:
    n = len(seats)
    
    empty_positions = [i for i, ch in enumerate(seats) if ch == '0']
    
    if not empty_positions:
        return None
    
    best_pos = None
    best_threats = float('inf')
    
    for pos in empty_positions:
        left_threats = 0
        for i in range(pos - 1, -1, -1):
            if seats[i] == ' ':
                break
            if seats[i] in ('0', '1'):
                left_threats += 1
                break
        
        right_threats = 0
        for i in range(pos + 1, n):
            if seats[i] == ' ':
                break
            if seats[i] in ('0', '1'):
                right_threats += 1
                break
        
        total_threats = left_threats + right_threats
        
        if total_threats >= 2:
            continue
        
        if total_threats < best_threats:
            best_threats = total_threats
            best_pos = pos
    
    if best_pos is None:
        return None
    
    result = list(seats)
    result[best_pos] = '1'
    return ''.join(result)
