def cake_visualizer(s):
    lines = s.split('\n')
    result = []
    
    for line in lines:
        if not line.strip():
            result.append('')
            continue
            
        first_idx = next(i for i, c in enumerate(line) if c != ' ')
        last_idx = len(line) - next(i for i, c in enumerate(line[::-1]) if c != ' ') - 1
        
        first_char = line[first_idx]
        last_char = line[last_idx]
        middle_len = last_idx - first_idx - 1
        
        if middle_len <= 0:
            new_line = line
        else:
            left_pad = first_idx
            left_part = ' ' * left_pad + first_char
            middle_part = ' ' * (middle_len // 2) + '|' + ' ' * (middle_len - middle_len // 2 - 1)
            right_part = last_char
            
            new_line = left_part + middle_part + right_part
            
        result.append(new_line.rstrip())
        
    return "\n".join(result)
