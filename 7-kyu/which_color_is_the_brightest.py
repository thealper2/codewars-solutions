def brightest(colors):
    max_val = float('-inf')
    max_color = None
    for color in colors:
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        value = max(r, g, b)
        if value > max_val:
            max_val = value
            max_color = color
        
    return max_color
