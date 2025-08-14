def check_sequence(sequence, l, n):
    if not sequence:
        return False
    
    streaks = []
    current_char = sequence[0]
    current_length = 1
    
    for char in sequence[1:]:
        if char == current_char:
            current_length += 1
        else:
            streaks.append(current_length)
            current_char = char
            current_length = 1
    streaks.append(current_length)
    
    count = 0
    for length in streaks:
        if length == l:
            count += 1
    
    return count == n
