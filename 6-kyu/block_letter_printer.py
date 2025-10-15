 from preloaded import ALPHA

def block_print(s):
    s = s.strip().upper()
    if not s:
        return ''
    
    lines = [''] * 7
    for c in s:
        for i in range(7):
            if c == ' ':
                lines[i] += ' ' * 5
            else:
                lines[i] += ALPHA[c.lower()][i]
                
            lines[i] += ' '
                
    lines = [line.rstrip() for line in lines]
    return '\n'.join(lines)
