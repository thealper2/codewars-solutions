def tab_to_spaces(text):
    lines = text.split('\n')
    result = []
    for line in lines:
        new_line = []
        col = 0
        for char in line:
            if char == '\t':
                spaces = 4 - (col % 4)
                new_line.append(' ' * spaces)
                col += spaces
            else:
                new_line.append(char)
                col += 1
                
        result.append(''.join(new_line))
    
    return '\n'.join(result)
