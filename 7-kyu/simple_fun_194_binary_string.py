def bin_str(s):
    flips = 0
    flip_flag = False
    for char in s:
        current = char
        if flip_flag:
            current = '1' if current == '0' else '0'
        if current == '1':
            flips += 1
            flip_flag = not flip_flag
    return flips
