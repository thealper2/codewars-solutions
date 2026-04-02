def pos_average(s):
    words = s.split(', ')
    n = len(words)
    
    if n < 2:
        return 0.0
    
    str_length = len(words[0])
    
    total_pairs = n * (n - 1) // 2
    total_positions = total_pairs * str_length
    
    matching_positions = 0
    
    for pos in range(str_length):
        freq = {}
        for word in words:
            char = word[pos]
            freq[char] = freq.get(char, 0) + 1
        
        for count in freq.values():
            if count > 1:
                matching_positions += count * (count - 1) // 2
    
    percentage = (matching_positions * 100.0) / total_positions
    return round(percentage, 10)
