def frame(text, char):
    n = len(text)
    max_len = max(len(w) for w in text) + 4
    t = ''.join(text)
    frame = [f'{char}' * max_len]
    
    for i in range(n):
        row = [f'{char}', ' ']
        row.extend(list(text[i]))
        row.extend([' '] * (max_len - len(text[i]) - 3))
        row.extend(f'{char}')
        frame.append(''.join(row))
    
    frame.append(f'{char}' * max_len)
    return '\n'.join(frame)
