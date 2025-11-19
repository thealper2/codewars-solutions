def get_rectangle_string(width, height):
    lines = []
    for i in range(height):
        if i == 0 or i == height - 1:
            line = '*' * width
        else:
            if width >= 2:
                line = '*' + ' ' * (width - 2) + '*'
            else:
                line = '*'
            
        lines.append(line)
        
    return '\r\n'.join(lines) + '\r\n'
