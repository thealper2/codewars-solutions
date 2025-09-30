def parse_html_color(color):
    color = color.lower()
    color = PRESET_COLORS.get(color, color)
    if color.startswith('#'):
        hex_code = color[1:]
    else:
        hex_code = color
        
    if len(hex_code) == 3:
        hex_code = ''.join(c * 2 for c in hex_code)
        
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return {'r': r, 'g': g, 'b': b}
