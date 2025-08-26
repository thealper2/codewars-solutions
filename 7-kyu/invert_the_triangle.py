def invert_triangle(triangle):
    result = []
    lines = triangle.split('\n')
    for line in lines:
        new_line = ''
        for c in line:
            if c == ' ':
                new_line += '#'
            elif c == '#':
                new_line += ' '
                
        result.append(new_line)
        
    return '\n'.join(result[::-1])
