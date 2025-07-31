def shades_of_grey(n):
    if n <= 0:
        return []
    
    max_shades = 254
    n = min(n, max_shades)
    shades = []
    for i in range(1, n + 1):
        hex_part = format(i, '02x')
        shades.append(f'#{hex_part * 3}')
    
    return shades
