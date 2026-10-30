def hex_string_to_RGB(hex_string):
    h = hex_string.lstrip('#')
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return {'r': r, 'g': g, 'b': b}