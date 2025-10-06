def custom_christmas_tree(chars, n):
    result = []
    char_index = 0
    total_chars = len(chars)
    for i in range(1, n + 1):
        line_chars = []
        for j in range(i):
            line_chars.append(chars[char_index % total_chars])
            char_index += 1
            
        line = ' ' * (n - i) + ' '.join(line_chars)
        result.append(line)
        
    trunk_height = n // 3
    trunk_spaces = ' ' * (n - 1)
    for _ in range(trunk_height):
        result.append(trunk_spaces + '|')
        
    return '\n'.join(result)
