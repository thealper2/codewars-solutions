def scale(strng, k, v):
    if not strng:
        return ""
    
    lines = strng.split('\n')
    scaled_h = []
    for line in lines:
        new_line = ''.join([c * k for c in line])
        scaled_h.append(new_line)
    
    scaled_v = []
    for line in scaled_h:
        scaled_v.extend([line] * v)

    return '\n'.join(scaled_v)
