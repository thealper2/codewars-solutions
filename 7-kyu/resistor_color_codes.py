def decode_resistor_colors(bands):
    color_codes = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'gray': 8,
        'white': 9
    }
    
    tolerance_map = {
        'gold': '5',
        'silver': '10',
        '': '20'
    }
    
    bands_list = bands.split()
    num_bands = len(bands_list)
    
    first = color_codes[bands_list[0]]
    second = color_codes[bands_list[1]]
    third = color_codes[bands_list[2]]
    
    if num_bands >= 4:
        tolerance_band = bands_list[3]
    else:
        tolerance_band = ''
    
    ohms = (first * 10 + second) * (10 ** third)
    tolerance = tolerance_map.get(tolerance_band, '20')
    
    if ohms < 1000:
        value_str = str(ohms)
    elif ohms < 1000000:
        value = ohms / 1000.0
        value_str = str(int(value)) if value.is_integer() else f"{value:.1f}".rstrip('0').rstrip('.')
        value_str += "k"
    else:
        value = ohms / 1000000.0
        value_str = str(int(value)) if value.is_integer() else f"{value:.1f}".rstrip('0').rstrip('.')
        value_str += "M"
    
    return f"{value_str} ohms, {tolerance}%"
